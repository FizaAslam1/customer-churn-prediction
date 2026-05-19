📊 Telecom Customer Churn Prediction App

Predict which customers are about to leave — before it's too late.

🌐 Live Demo: Click Here to Try the App
💻 GitHub: FizaAslam1/customer-churn-prediction

🎯 Problem Statement
Telecom companies lose millions of dollars every year due to customer churn.
The challenge? They don't know WHO is going to leave — until it's too late.
This ML-powered app predicts which customers are at risk of churning based on their account behavior, services used, and billing patterns — so businesses can take action before losing them.

🚀 What It Does

Takes customer data as input (demographics, services, billing)
Predicts: Will this customer churn? Yes or No
Shows prediction confidence score
Helps telecom businesses retain valuable customers


✨ Features
FeatureDescription🔮 Churn PredictionPredicts churn probability for any customer📊 Interactive DashboardClean Streamlit UI for easy input💡 Confidence ScoreShows how confident the model is📈 Feature ImportanceWhich factors matter most for churn

📊 Model Performance
MetricValueAlgorithmRandom Forest / Logistic RegressionAccuracy78%Precision65%Recall57%F1-Score61%

🔍 Features Used
👤 Customer Demographics

Gender, Senior Citizen, Partner, Dependents

📋 Account Information

Tenure, Contract Type, Payment Method

📡 Services

Phone, Internet, Security, Backup, Streaming

💰 Billing Details

Monthly Charges, Total Charges


🛠️ Tech Stack
ToolPurposePythonCore programmingScikit-learnML model buildingPandas & NumPyData preprocessingStreamlitInteractive web appMatplotlib & SeabornData visualization

📁 Project Structure
customer-churn-prediction/
│
├── app.py                  # Streamlit app
├── model.pkl               # Trained ML model
├── requirements.txt        # Dependencies
├── churn_data.csv          # Dataset
└── README.md               # Project documentation

🎮 How To Run Locally
bash# Clone the repository
git clone https://github.com/FizaAslam1/customer-churn-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

💼 Use Cases

📡 Telecom Companies — Identify at-risk customers early
🏦 Banks & Fintech — Predict account closures
🛒 E-commerce — Reduce subscriber dropoff
📊 Business Analytics — Customer retention strategy


👩‍💻 About
Built by Fiza Aslam — BS IT Student & Aspiring Data Scientist
📍 The Islamia University of Bahawalpur, Pakistan
🔗 LinkedIn | GitHub | Kaggle
