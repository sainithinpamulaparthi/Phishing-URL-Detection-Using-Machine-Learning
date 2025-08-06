Phishing-URL-Detection-Using-Machine-Learning 🎣
A web application that uses machine learning to detect phishing URLs in real-time. This tool helps users identify potentially malicious websites before visiting them, enhancing online security.

✨ Features
Real-Time Detection: Instantly classify URLs as "Legitimate" or "Phishing".

Machine Learning Powered: Utilizes a RandomForestClassifier for high accuracy.

User-Friendly Interface: Clean, modern, and easy-to-use web interface built with Flask.

Efficient Model Loading: The trained model is saved and loaded on startup, eliminating the need for retraining.

Secure Session Management: Includes a simple login/logout flow to simulate a real-world application.

🛠️ Tech Stack
Backend: Python, Flask

Machine Learning: Scikit-learn, Pandas, Joblib

Frontend: HTML, CSS

🚀 Getting Started
Follow these steps to get the project up and running on your local machine.

Prerequisites
Python 3.x

pip (Python package installer)

Installation & Setup
Clone the repository:

git clone https://github.com/sainithinpamulaparthi/Phishing-URL-Detection-Using-Machiine-Learning.git
cd phishing-url-detector

Install the required libraries:

pip install -r requirements.txt

Place the dataset:
Make sure the phishing_site_urls.csv file is in the root directory of the project.

Run the application:

python web_app.py

Access the application:
Open your web browser and navigate to http://127.0.0.1:5000.

⚙️ How It Works
The application's core logic involves a few key steps:

Feature Extraction: When a user submits a URL, its structural properties (like URL length, presence of an IP address, use of hyphens, etc.) are converted into a numerical feature set.

Model Prediction: These features are fed into the pre-trained Random Forest model.

Classification: The model classifies the URL as either Legitimate (0) or Phishing (1).

Display Result: The result is then displayed to the user on the web interface.

The model is trained only once (the first time the app runs) and then saved as phishing_model.joblib for instant loading in future sessions.
