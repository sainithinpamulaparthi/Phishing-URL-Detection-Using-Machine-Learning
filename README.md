Phishing URL Detection Using Machine Learning
A robust and real-time machine learning solution to detect phishing URLs and safeguard users from cyber threats.

🚩 Project Overview
Phishing attacks remain one of the most prevalent cybersecurity threats, where attackers spoof legitimate websites to steal sensitive data. This project implements advanced machine learning models to classify URLs as phishing or legitimate, improving detection accuracy beyond traditional blacklist methods.

💡 Features
Automatic phishing URL classification based on extracted URL characteristics.

Multiple machine learning models implemented: Logistic Regression, Random Forest, SVM.

High classification accuracy (up to 98.5%) on benchmark datasets.

Real-time detection with responsive web interface and command-line tools.

Modular codebase making it easy to extend and improve.

Privacy-conscious: processes URLs without collecting personal data.

📂 Dataset
Collected from trusted public source Kaggle.

Features extracted include: URL length, special characters, subdomain count, use of IP addresses, HTTPS presence, and domain age.

🛠️ Installation
bash
git clone https://github.com/sainithinpamulaparthi/phishing-url-detection
cd phishing-url-detection-using-machine-learning
pip install -r requirements.txt
🚀 Usage
Jupyter Notebook:
Run the step-by-step notebook Phishing_Detection.ipynb for detailed analysis and model training.

Web Application:
Start the Flask app:

bash
python app.py
Open your browser at http://localhost:5000 to interact with the detection tool.

Command-Line Interface:
Use scripts in src/ to test URLs individually or in batch mode.

📊 Model Performance
Model	Accuracy	Precision	Recall	F1-Score
Logistic Regression	98.1%	97.5%	98.0%	97.7%
Random Forest	98.5%	97.8%	98.1%	97.9%
SVM	98.0%	97.2%	97.9%	97.5%
📁 Project Structure
text
phishing-url-detection/
├── assets/            # Images, screenshots
├── data/              # Raw & processed datasets
├── notebooks/         # Exploratory Data Analysis & modeling
├── src/               # Core modules & scripts
├── app.py             # Flask web app main file
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
🤝 Contributing
Contributions are welcome! Feel free to:

Fork the repo

Create a feature branch

Submit pull requests

Report issues or suggest enhancements

📃 License
This project is licensed under the MIT License. See LICENSE for details.

🙋 Contact
Project Maintainer: [Sai Nithin Pamulaparthi]
Email: nithu772005@gmail.com
Feel free to reach out for collaboration or queries.

⭐ If you find this project useful, please star the repository!
