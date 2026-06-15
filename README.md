 🩺 Diabetes Risk Predictor

A Machine Learning-powered healthcare analytics application that predicts an individual's diabetes risk based on medical and lifestyle parameters.
The application leverages multiple Machine Learning algorithms, automatically selects the best-performing model, and provides interactive risk analysis, visual dashboards, personalized health recommendations, and downloadable PDF reports.

🚀 Project Overview

Diabetes is one of the most prevalent chronic diseases worldwide. Early risk assessment can help individuals take preventive measures before the condition becomes severe.
This project uses Machine Learning techniques to analyze patient health data and estimate the likelihood of diabetes. The system provides a user-friendly web interface where users can input health parameters and receive an instant risk assessment.

🎯 Objectives

1.Predict diabetes risk using Machine Learning
2.Compare multiple classification algorithms
3.Visualize healthcare data through interactive dashboards
4.Generate personalized health recommendations
5.Produce downloadable PDF reports
6.Provide an intuitive and professional healthcare interface

 ✨ Features

1.🔍 Diabetes Risk Prediction

Predicts diabetes likelihood using patient health information.

2.📊 Risk Score Analysis

Displays prediction confidence through an interactive risk score gauge.

3.🧠 AI Risk Interpretation

Provides human-readable explanations of the predicted risk level.

4.📋 Personalized Recommendations

Generates health suggestions based on the user's risk category.

5.📈 Analytics Dashboard

Includes:

a.Outcome Distribution
b.Glucose Distribution
c.BMI Distribution
d.Age Distribution
e.Correlation Heatmap
f.Glucose vs BMI Analysis
g.Model Performance Comparison
h.Feature Importance Visualization


📄 PDF Report Generation

Creates downloadable patient reports containing:

1.Patient Details
2.Prediction Result
3.Risk Score

 📖 Health Reference Guide

Provides reference ranges and interpretations for:

1.Glucose
2.Blood Pressure
3.BMI
4.Insulin
5.Pregnancies
6.Skin Thickness
7.Diabetes Pedigree Function
8.Age

 📋 Live Health Analysis

Instantly evaluates health parameters before prediction.

 🏗️ System Architecture

User Input
↓
Data Validation
↓
Feature Scaling
↓
Machine Learning Model
↓
Risk Prediction
↓
Recommendations Engine
↓
Analytics Dashboard
↓
PDF Report Generation

 🧠 Machine Learning Models

The project trains and evaluates multiple Machine Learning algorithms.

1.Logistic Regression

a.Fast and efficient
b.Probabilistic output
c.Highly interpretable

2.Support Vector Machine (SVM)

a.Effective for classification tasks
b.Strong performance on structured datasets

3.Decision Tree

a.Easy to interpret
b.Captures non-linear relationships

The system automatically selects the best-performing model based on evaluation accuracy.


📂 Dataset

1.PIMA Indians Diabetes Dataset
Features:

a.Pregnancies
b.Glucose
c.Blood Pressure
d.Skin Thickness
e.Insulin
f.BMI
g.Diabetes Pedigree Function
h.Age

Target Variable:

a.0 → Non-Diabetic
b.1 → Diabetic

🛠️ Technology Stack

1.Programming Language
Python

2.Frontend
Streamlit

3.Machine Learning
Scikit-Learn

Data Processing
1.Pandas
2.NumPy

Visualization

1.Plotly
2.atplotlib
3.Seaborn

Report Generation
ReportLab

 Version Control

1.Git
2.GitHub

 📁 Project Structure
DiabetesRiskPredictor
│
├── app.py
├── train_model.py
├── recommendation.py
├── report_generator.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── diabetes.csv
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   ├── feature_names.pkl
│   └── accuracies.pkl
│
├── reports/
│
└── screenshots/

⚙️ Installation

1.Clone Repository

bash
git clone https://github.com/kripapatwari8-creator/DiabetesRiskPredictor.git

2.Navigate to Project

bash
cd DiabetesRiskPredictor

3.Create Virtual Environment

bash
python -m venv venv

4.Activate Virtual Environment

bash
venv\Scripts\activate

5.Install Dependencies

bash
pip install -r requirements.txt

6.Run Application

bash
streamlit run app.py

📸 Application Screenshots

1.Home Page
<img width="959" height="465" alt="Screenshot 2026-06-15 111733" src="https://github.com/user-attachments/assets/e37c739a-ec5f-4145-8920-b24998baa047" />

2.Prediction Result
<img width="958" height="431" alt="image" src="https://github.com/user-attachments/assets/f04924cd-326b-4a75-9d2e-a6a6fe87ee5c" />
<img width="958" height="497" alt="image" src="https://github.com/user-attachments/assets/f10fa6fb-20cd-4d58-936b-0a303599eaeb" />
<img width="953" height="460" alt="image" src="https://github.com/user-attachments/assets/c1c2f79b-0938-43d6-a63a-391e1bbb4ac8" />

3.Dashboard Analytics
<img width="958" height="448" alt="image" src="https://github.com/user-attachments/assets/421b71fc-4ae7-4794-bdb6-741334930a6e" />
<img width="959" height="346" alt="image" src="https://github.com/user-attachments/assets/7285a487-5ac4-4d6a-81fb-62d0da4b7509" />

4.Feature Importance Analysis
<img width="959" height="367" alt="image" src="https://github.com/user-attachments/assets/5b08515f-3f5e-4acf-a6a4-9f7e45cc2aac" />
<img width="959" height="500" alt="image" src="https://github.com/user-attachments/assets/6f745406-952d-4602-854c-72fb09c8ee6b" />
<img width="959" height="500" alt="image" src="https://github.com/user-attachments/assets/312451b5-6f6c-4d05-9fb9-7c8622a88428" />
<img width="634" height="473" alt="image" src="https://github.com/user-attachments/assets/834a14e7-3508-4bc1-aff5-9e902a6c9d38" />
<img width="871" height="356" alt="image" src="https://github.com/user-attachments/assets/81c8bac0-ba5a-4d4a-abc3-a4c565f8af4d" />

5.Model Comparison Dashboard
<img width="960" height="600" alt="image" src="https://github.com/user-attachments/assets/f64685ac-a6a3-48fc-b078-41d691ef59ac" />
<img width="959" height="503" alt="image" src="https://github.com/user-attachments/assets/7359ee27-9d56-4355-9978-0c5598890af7" />

6.PDF Report
<img width="391" height="500" alt="image" src="https://github.com/user-attachments/assets/eeb155d0-bbf9-4a91-be02-144d58e926d9" />
<img width="392" height="503" alt="image" src="https://github.com/user-attachments/assets/bc2adfa7-80c6-40a9-bab4-66a7317fb75d" />
<img width="394" height="244" alt="image" src="https://github.com/user-attachments/assets/34faf59c-3af7-43d1-bcea-4e66c57dc811" />

📊 Key Insights

1.Glucose is one of the strongest indicators of diabetes risk.
2.BMI and Age significantly influence prediction outcomes.
3.Multiple machine learning algorithms were evaluated to ensure reliable performance.
4.Interactive visualizations improve interpretability and user experience.

🔮 Future Enhancements

1.Explainable AI (SHAP)
2.User Authentication
3.Cloud Database Integration
4.Doctor Recommendation System
5.Medical History Tracking
6.Mobile Application Version
7.Real-Time Health Monitoring

📚 References

1. PIMA Indians Diabetes Dataset
2. Scikit-Learn Documentation
3. Streamlit Documentation
4. Pandas Documentation
5. Plotly Documentation
6. ReportLab Documentation


This project was developed as part of a Artificial Intelligence/Machine Learning internship to demonstrate practical applications of data science and predictive analytics in healthcare.
