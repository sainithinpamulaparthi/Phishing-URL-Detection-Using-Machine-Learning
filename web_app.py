# Import necessary libraries
import pandas as pd
import numpy as np
import re
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from urllib.parse import urlparse
from flask import Flask, request, render_template_string, redirect, url_for, session

# --- 1. Feature Extraction (Same as before) ---
def extract_features(url):
    features = {}
    if not url.startswith('http'):
        url = 'http://' + url
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
    except Exception:
        parsed_url = None
        domain = ''

    ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    features['having_IP_Address'] = 1 if ip_pattern.match(domain) else 0
    
    if len(url) < 54: features['URL_Length'] = 0
    elif 54 <= len(url) <= 75: features['URL_Length'] = 1
    else: features['URL_Length'] = 2

    shortening_services = ['bit.ly', 'goo.gl', 't.co', 'tinyurl.com']
    features['Shortening_Service'] = 1 if any(service in domain for service in shortening_services) else 0
    features['having_At_Symbol'] = 1 if '@' in url else 0
    features['double_slash_redirecting'] = 1 if url.rfind('//') > 6 else 0
    features['Prefix_Suffix'] = 1 if '-' in domain else 0
    
    num_dots = domain.count('.')
    if num_dots <= 2: features['having_Sub_Domain'] = 0
    elif num_dots == 3: features['having_Sub_Domain'] = 1
    else: features['having_Sub_Domain'] = 2
        
    return features

# --- 2. Model Training and Persistence (Same as before) ---
def load_or_train_model():
    model_path = 'phishing_model.joblib'
    columns_path = 'feature_columns.joblib'
    dataset_path = 'phishing_site_urls.csv'

    if os.path.exists(model_path) and os.path.exists(columns_path):
        print("Loading pre-trained model...")
        model = joblib.load(model_path)
        feature_columns = joblib.load(columns_path)
        return model, feature_columns

    print("No pre-trained model found. Starting training process...")
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset file '{dataset_path}' not found. Cannot train new model.")
        return None, None

    print(f"Loading dataset from '{dataset_path}'...")
    df = pd.read_csv(dataset_path)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df['Label'] = df['Label'].map({'bad': 1, 'good': 0})

    print("Extracting features... This might take a moment.")
    features_df = df['URL'].apply(lambda url: pd.Series(extract_features(url)))
    X = features_df
    y = df['Label']
    
    print("Training the model on the full dataset...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X, y)
    print("Model training complete.")

    joblib.dump(model, model_path)
    joblib.dump(X.columns, columns_path)
    print(f"Model saved to '{model_path}'")
    
    return model, X.columns

# --- 3. Flask Web Application ---
app = Flask(__name__)
app.secret_key = 'a_very_secret_key_for_sessions' # Needed for session management

model, feature_columns = load_or_train_model()

# UPDATED: HTML Template for the Login Page
LOGIN_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phishing Detector Login</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Roboto', sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .login-container { background-color: white; padding: 40px 30px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); width: 100%; max-width: 400px; }
        h1 { text-align: center; color: #333; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 5px; color: #555; font-weight: bold; }
        .form-group input[type="text"], .form-group input[type="password"] { width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; }
        .form-options { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; font-size: 14px; }
        .login-btn { width: 100%; padding: 12px; background-color: #28a745; border: none; color: white; font-size: 16px; font-weight: bold; border-radius: 5px; cursor: pointer; transition: background-color 0.3s; }
        .login-btn:hover { background-color: #218838; }
        .signup-link { text-align: center; margin-top: 20px; font-size: 14px; }
        .signup-link a { color: #28a745; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Phishing Detector Login</h1>
        <form action="/login" method="post">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-options">
                <label><input type="checkbox" name="remember" checked> Remember me</label>
            </div>
            <button type="submit" class="login-btn">Login</button>
        </form>
        <div class="signup-link">
            Don't have an account? <a href="#">Sign up</a>
        </div>
    </div>
</body>
</html>
"""

# UPDATED: HTML Template for the URL Checker Page
CHECKER_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phishing URL Detector</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Roboto', sans-serif; background-color: #f8f9fa; margin: 0; padding: 20px; }
        .header { display: flex; justify-content: space-between; align-items: center; max-width: 800px; margin: 0 auto 40px; }
        .header h1 { font-size: 24px; font-weight: bold; color: #333; }
        .logout-btn { background-color: #dc3545; color: white; padding: 8px 16px; border: none; border-radius: 5px; cursor: pointer; text-decoration: none; font-size: 14px; font-weight: bold; }
        .container { background-color: white; padding: 40px; border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.1); max-width: 800px; margin: 0 auto; }
        h2 { text-align: center; color: #333; margin-bottom: 25px; }
        form { display: flex; flex-direction: column; align-items: center; }
        input[type="text"] { width: 100%; padding: 15px; margin-bottom: 20px; border: 1px solid #dee2e6; border-radius: 8px; font-size: 16px; box-sizing: border-box; }
        input[type="submit"] { background-color: #28a745; color: white; padding: 12px 25px; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: bold; }
        .result { margin-top: 30px; padding: 20px; border-radius: 8px; font-size: 20px; font-weight: bold; }
        .phishing { background-color: #f8d7da; color: #721c24; }
        .legitimate { background-color: #d4edda; color: #155724; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Welcome, {{ username }}!</h1>
        <a href="/logout" class="logout-btn">Logout</a>
    </div>
    <div class="container">
        <h2>Phishing URL Detector</h2>
        <form action="/predict" method="post">
            <input type="text" name="url" placeholder="https://www.youtube.com/" required>
            <input type="submit" value="Check URL">
        </form>
        {% if result %}
        <div class="result {{ 'phishing' if 'Phishing' in result else 'legitimate' }}">
            <p>Result: {{ result }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def login_page():
    return render_template_string(LOGIN_HTML)

@app.route('/login', methods=['POST'])
def handle_login():
    # Store username in session. In a real app, you'd validate the password.
    session['username'] = request.form.get('username', 'admin')
    return redirect(url_for('checker_page'))

@app.route('/checker', methods=['GET'])
def checker_page():
    if 'username' not in session:
        return redirect(url_for('login_page'))
    return render_template_string(CHECKER_HTML, username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_page'))

@app.route('/predict', methods=['POST'])
def predict():
    if 'username' not in session:
        return redirect(url_for('login_page'))
    if model is None or feature_columns is None:
        return render_template_string(CHECKER_HTML, username=session['username'], result="Model is not trained.")

    url_to_check = request.form['url']
    if not url_to_check:
        return redirect(url_for('checker_page'))

    features = extract_features(url_to_check)
    features_df = pd.DataFrame([features], columns=feature_columns)
    
    prediction = model.predict(features_df)
    
    result_text = "Phishing" if prediction[0] == 1 else "Legitimate"
    
    return render_template_string(CHECKER_HTML, username=session.get('username', 'Guest'), result=result_text)

# --- Main Execution ---
if __name__ == "__main__":
    if model is None:
        print("Failed to load or train the model. The web application cannot start.")
    else:
        print("Model loaded successfully. Starting Flask server...")
        app.run(host='0.0.0.0', port=5000, debug=False)
