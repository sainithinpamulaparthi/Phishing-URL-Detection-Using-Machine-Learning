# Phishing URL Detection Using Machine Learning 🎣

This repository contains the source code for a web application that uses machine learning to detect phishing URLs in real-time. The goal is to provide a simple yet powerful tool for users to verify the safety of a URL before clicking on it.

---

### 🎯 **Project Goal**

The main objective is to build and deploy a robust application that leverages a `RandomForestClassifier` to achieve high accuracy in identifying phishing attempts. This project serves as a practical implementation of machine learning for a real-world cybersecurity problem.

---

### 🗂️ **Project Modules**

| # | Module | Status | Description |
| :--- | :--- | :--- | :--- |
| 1 | **Feature Extraction** | ✅ | Logic to convert URL strings into numerical features based on structural properties (e.g., length, IP address, special characters). |
| 2 | **Model Training** | ✅ | A `RandomForestClassifier` is trained on the `phishing_site_urls.csv` dataset and saved as `phishing_model.joblib`. |
| 3 | **Web Interface** | ✅ | A user-friendly front-end built with Flask that includes a secure login, a URL submission form, and a results display. |
| 4 | **Prediction API** | ✅ | A Flask route that handles incoming URL submissions, processes them through the model, and returns a classification. |

---

### 📂 **File Structure**

| File | Purpose |
| :--- | :--- |
| `web_app.py` | The main Python script that contains all the Flask routes and machine learning logic. |
| `phishing_site_urls.csv` | The dataset used to train the machine learning model. |
| `requirements.txt` | A list of all the Python libraries required to run the project. |
| `phishing_model.joblib` | The pre-trained and saved machine learning model file for instant loading. |
| `feature_columns.joblib`| Stores the feature names to ensure consistency between training and prediction. |
| `README.md` | This file, providing a comprehensive overview of the project. |

---

### 🚀 **How to Run**

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/sainithinpamulaparthi/phishing-url-detection-using-machine-learning.git](https://github.com/sainithinpamulaparthi/phishing-url-detection-using-machine-learning.git)
    cd phishing-url-detector
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Flask App:**
    ```bash
    python web_app.py
    ```

4.  **Access in Browser:**
    Open your web browser and go to `http://127.0.0.1:5000`.

---

### 📚 **Technologies & Resources**

* **Backend**: [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/)
* **Machine Learning**: [Scikit-learn](https://scikit-learn.org/), [Pandas](https://pandas.pydata.org/), [Joblib](https://joblib.readthedocs.io/)
* **Dataset**: [Phishing Site URLs on Kaggle](https://www.kaggle.com/datasets/eswarchandt/phishing-website-detector)

---

### 💡 **Final Thoughts**

> "The best defense against cyber threats is a combination of user awareness and intelligent tools. This project aims to be one of those tools."
