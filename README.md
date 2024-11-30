# Facial Recognition and Analysis with AWS Rekognition

This project demonstrates how to perform **Facial Recognition** and **Facial Analysis** using **AWS Rekognition**. The application is a simple yet powerful implementation that utilizes **Flask** for the web interface and **boto3** for AWS interactions.

## 📹 Video Tutorial

For detailed step-by-step instructions, watch the YouTube video here:  
👉 [YouTube Tutorial Link](https://youtu.be/_6_7hK9Xad0)

---

## 🚀 Getting Started

### Requirements

- **Python Packages**:
  - `boto3`
  - `Flask`
- **AWS Account**:
  - Access to AWS Rekognition and S3 services.

---

### ⚙️ Setup Instructions

1. **Create an IAM User**:
   - Log in to your AWS Console.
   - Go to **IAM Management Console**.
   - Create a user with:
     - **S3 Full Access**
     - **Rekognition Full Access**
   - Generate **Access Keys** (Access Key ID and Secret Access Key).

2. **Pre-Configuration**:
   - Clone this repository and open the project in your local environment.
   - Open the `recognition.ipynb` file and run the cells step by step.
   - In the **AWS Configure** cell:
     - Enter your **Access Key ID** and **Secret Access Key**.
     - Leave other fields (e.g., default region) as default by pressing `Enter`.

3. **Setup AWS Rekognition and S3**:
   - Create an **S3 Bucket** for storing images.
   - Create a **Face Collection** in AWS Rekognition for indexing faces.
   - Uploading images to S3 is optional; you can index faces directly later through the web application.

4. **Run the Application**:
   - Execute `app.py` to start the Flask web application.
   - The web app allows you to:
     - Index faces.
     - Perform facial recognition and analysis.
     - View detailed results.

---

### 📂 Files in the Repository

- **recognition.ipynb**: Pre-configuration script for AWS setup.
- **app.py**: Flask-based web application for face recognition and analysis.
- **requirements.txt**: List of required Python packages.

---

### 🛠 Tools and Technologies

- AWS Rekognition
- AWS S3
- Flask
- Python (boto3)

---

### 📹 Watch the Video

[Complete Tutorial Video](https://youtu.be/_6_7hK9Xad0)

---

### 💻 Contribute

Feel free to contribute to this project by opening issues or submitting pull requests. Let’s make this application even better!

---

### 📧 Contact

For queries, reach out via [YouTube comments](https://youtu.be/_6_7hK9Xad0) or open an issue on GitHub.  

---

#### ⭐ Don’t forget to star this repository if you found it helpful! 🎉
