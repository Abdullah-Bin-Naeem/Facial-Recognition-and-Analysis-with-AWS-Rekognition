from flask import Flask, request, render_template, jsonify
import boto3
import os

app = Flask(__name__)

# Initialize Rekognition client
rekognition_client = boto3.client('rekognition', region_name='ap-south-1')

# S3 Bucket for storing images
S3_BUCKET = 'my-unique-images-bucket'

# Rekognition Collection ID
COLLECTION_ID = 'my-face-collection'

# Routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    # Upload image to S3 and index it
    image = request.files['image']
    external_image_id = request.form['name']
    file_path = os.path.join('uploads', image.filename)
    image.save(file_path)

    s3_client = boto3.client('s3', region_name='ap-south-1')
    s3_client.upload_file(file_path, S3_BUCKET, image.filename)

    try:
        # Index the face into the collection
        response = rekognition_client.index_faces(
            CollectionId=COLLECTION_ID,
            Image={'S3Object': {'Bucket': S3_BUCKET, 'Name': image.filename}},
            ExternalImageId=external_image_id,
            DetectionAttributes=['ALL']
        )
        os.remove(file_path)

        # Check if faces were successfully indexed
        if response['FaceRecords']:
            return render_template('upload_result.html', success=True)
        else:
            return render_template('upload_result.html', success=False)

    except Exception as e:
        print(f"Error indexing face: {e}")
        os.remove(file_path)
        return render_template('upload_result.html', success=False)

@app.route('/search', methods=['POST'])
@app.route('/search', methods=['POST'])
def search_face():
    # Search for the uploaded face in the collection
    image = request.files['image']
    file_path = os.path.join('uploads', image.filename)
    image.save(file_path)

    s3_client = boto3.client('s3', region_name='ap-south-1')
    s3_client.upload_file(file_path, S3_BUCKET, image.filename)

    image_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{image.filename}"
    print(f"Generated Image URL: {image_url}")

    response = rekognition_client.search_faces_by_image(
        CollectionId=COLLECTION_ID,
        Image={'S3Object': {'Bucket': S3_BUCKET, 'Name': image.filename}},
        MaxFaces=5,
        FaceMatchThreshold=90
    )

    os.remove(file_path)

    if response['FaceMatches']:
        top_match = max(response['FaceMatches'], key=lambda x: x['Similarity'])
        external_id = top_match['Face']['ExternalImageId']
        similarity = top_match['Similarity']

        return render_template(
            'search_result.html',
            external_id=external_id,
            similarity=similarity,
            image_url=image_url
        )
    else:
        return jsonify({'status': 'No matches found', 'response': response})

@app.route('/analyze', methods=['POST'])
def analyze_face():
    # Analyze facial features of the uploaded image
    image = request.files['image']
    file_path = os.path.join('uploads', image.filename)
    image.save(file_path)

    s3_client = boto3.client('s3', region_name='ap-south-1')
    s3_client.upload_file(file_path, S3_BUCKET, image.filename)

    image_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{image.filename}"

    response = rekognition_client.detect_faces(
        Image={'S3Object': {'Bucket': S3_BUCKET, 'Name': image.filename}},
        Attributes=['ALL']
    )

    os.remove(file_path)

    # Extract facial features from response
    features = {}
    if 'FaceDetails' in response and len(response['FaceDetails']) > 0:
        face_details = response['FaceDetails'][0]
        features['Age Range'] = f"{face_details['AgeRange']['Low']} - {face_details['AgeRange']['High']}"
        features['Emotions'] = ', '.join([emotion['Type'] for emotion in face_details['Emotions'] if emotion['Confidence'] > 50])
        features['Smile'] = "Yes" if face_details['Smile']['Value'] else "No"
        features['Eyeglasses'] = "Yes" if face_details['Eyeglasses']['Value'] else "No"

    return render_template('analyze_result.html', image_url=image_url, features=features)


if __name__ == '__main__':
    # Create uploads folder if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    # Run the app
    app.run(debug=True)
