# Credit Card Fraud Detection System

An End-to-End Machine Learning project designed to detect fraudulent credit card transactions in real-time. This repository covers everything from exploratory data analysis (EDA) and model training to cloud deployment.

## 🚀 Live Application
Check out the live interactive web app here: 
👉 https://credit-card-fraud-detection-pz9mwdjrptcpbqgd2htgm9.streamlit.app/

## 📌 Project Overview
Credit card fraud is a significant financial threat. This project builds a robust predictive system that analyzes transaction parameters and classifies them as either **Genuine** or **Fraudulent** instantly. The model has been saved, optimized, and deployed as a scalable web service.

## 🛠️ Tech Stack, Tools & Environments
* **Development Environments:** Google Colab (Model Training) & VS Code (App Development)
* **Programming Language:** Python
* **Machine Learning Library:** Scikit-Learn
* **Data Analysis & Visualization:** Pandas, NumPy, Matplotlib, Seaborn
* **Deployment Platform:** Streamlit Cloud

## 📁 Repository Structure & Workflow
* `Credit_Card_Fraud_Detection.ipynb` - Developed in **Google Colab**, this Jupyter Notebook contains data preprocessing, exploratory data analysis, and model training logic.
* `app.py` - Built using **VS Code**, this Python script powers the Streamlit web application interface and backend prediction logic.
* `fraud_model.pkl` - The trained Machine Learning model serialized using Pickle.
* `scaler.pkl` - The fitted StandardScaler instance used to normalize real-time user inputs.
* `requirements.txt` - Configuration file listing all necessary Python dependencies required to run the application on Streamlit Cloud.

## ⚙️ Key Features
* **Real-Time Predictions:** Users can input transaction details (Time, Amount, etc.) and get instant classification results.
* **Highly Responsive UI:** Built with Streamlit for a clean, user-friendly, and lightweight experience.
* **Pre-scaled Inputs:** Embedded scaler ensures that live user data is processed exactly like the training data to maintain prediction accuracy.
