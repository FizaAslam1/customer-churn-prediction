# 📊 Telecom Customer Churn Prediction

> Harness the power of machine learning to predict and prevent customer churn — transforming data into actionable retention strategies.

---

## 🎯 Executive Summary

Customer churn is one of the most significant challenges facing the telecom industry, costing companies millions in lost revenue annually. This advanced machine learning application enables businesses to identify at-risk customers and implement data-driven retention strategies.

**Live Demo:** [Try the Interactive App](https://customer-churn-prediction-kr8rlyy5c3ecmvexc7iumv.streamlit.app/)

---

## 🚀 Key Features

| Feature | Description |
|---------|-----------|
| 🔮 **Predictive Analytics** | Accurately identifies customers at risk of churning with confidence scores |
| 📊 **Interactive Dashboard** | Intuitive Streamlit interface for real-time predictions and insights |
| 💡 **Model Transparency** | Displays feature importance and key decision factors |
| 📈 **Comprehensive Analysis** | Evaluates demographics, service usage, billing patterns, and engagement metrics |
| ⚡ **Fast Inference** | Quick predictions on new customer data |
| 🎨 **Beautiful Visualizations** | Interactive charts and graphs for better understanding |

---

## 📈 Model Performance

Our ensemble model (Random Forest + Logistic Regression) delivers excellent results:

| Metric | Score |
|--------|-------|
| **Accuracy** | 78% |
| **Precision** | 65% |
| **Recall** | 57% |
| **F1-Score** | 61% |
| **AUC-ROC** | 0.82 |

---

## 📊 Predictive Variables

The model analyzes four key data dimensions:

### 👤 Customer Demographics
- Gender
- Senior Citizen Status
- Partner & Dependent Information
- Age Group

### 📋 Account Intelligence
- Tenure (Customer lifetime)
- Contract Type (Month-to-month, One year, Two year)
- Payment Method
- Internet Service Type (Fiber optic, DSL, No internet)
- Paperless Billing Status

### 📡 Service Engagement
- Phone Service
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies

### 💰 Financial Metrics
- Monthly Charges
- Total Charges
- Payment History

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.x |
| **ML Framework** | Scikit-learn |
| **Data Processing** | Pandas, NumPy |
| **Web Interface** | Streamlit |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Version Control** | Git & GitHub |

---

## ⚡ Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/FizaAslam1/customer-churn-prediction

# Navigate to project directory
cd customer-churn-prediction

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Launch the Streamlit application
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`

---

## 📁 Project Structure

```
customer-churn-prediction/
├── notebooks/                    # Jupyter notebooks for EDA and model development
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_data_preprocessing.ipynb
│   └── 03_model_training.ipynb
├── data/                         # Datasets
│   ├── raw/                      # Original datasets
│   ├── processed/                # Cleaned and preprocessed data
│   └── churn_data.csv
├── models/                       # Trained model files
│   ├── random_forest_model.pkl
│   ├── logistic_regression_model.pkl
│   └── scaler.pkl
├── src/                          # Source code modules
│   ├── data_processing.py
│   ├── model_training.py
│   └── utils.py
├── app.py                        # Main Streamlit application
├── requirements.txt              # Project dependencies
├── config.py                     # Configuration settings
└── README.md                     # This file
```

---

## 🔄 How It Works

### Workflow Process

1. **Data Input** 
   - User enters customer information (demographics, services, billing)

2. **Feature Processing** 
   - Automated data validation
   - Feature scaling and normalization
   - One-hot encoding for categorical variables

3. **Model Inference** 
   - Ensemble model generates prediction
   - Calculates churn probability

4. **Results Visualization** 
   - Displays confidence score
   - Shows key risk factors
   - Provides actionable recommendations

### Prediction Logic

The model analyzes historical patterns to identify behavioral indicators of churn:
- **Service Cancellations**: Customers canceling services are at higher risk
- **Payment Issues**: Late payments correlate with increased churn
- **Contract Type**: Month-to-month customers are more likely to churn
- **Tenure**: Newer customers have higher churn risk
- **Engagement**: Lower service usage indicates potential churn

---

## 💼 Industry Applications

This solution is applicable across multiple sectors:

- **📡 Telecom Providers** 
  - Identify and retain at-risk subscribers
  - Optimize pricing strategies
  - Design targeted retention campaigns

- **🏦 Financial Services** 
  - Predict account closures
  - Manage customer relationships
  - Reduce revenue leakage

- **🛒 Subscription Platforms** 
  - Reduce customer dropoff
  - Optimize retention campaigns
  - Improve lifetime value

- **📊 Enterprise Analytics** 
  - Develop data-driven retention strategies
  - Allocate resources efficiently
  - Maximize customer satisfaction

---

## 📊 Data Requirements

To use this model, provide the following customer information:

- **Required**: Demographics, Account tenure, Contract type, Payment method
- **Optional**: Service subscriptions, Usage patterns, Customer feedback

All data should be in tabular format (CSV, Excel, or database export).

---

## 🚀 Future Enhancements

- [ ] Deep Learning models (Neural Networks)
- [ ] Real-time batch prediction API
- [ ] Customer segmentation analysis
- [ ] Automated retention recommendation engine
- [ ] Mobile app integration
- [ ] Advanced visualization dashboard
- [ ] Multi-language support

---

## 🐛 Troubleshooting

**Issue**: Port 8501 already in use
```bash
streamlit run app.py --server.port=8502
```

**Issue**: Missing dependencies
```bash
pip install -r requirements.txt --upgrade
```

**Issue**: Model file not found
- Ensure all `.pkl` files are in the `models/` directory
- Re-run model training if files are missing

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Report Issues
- Report bugs via [GitHub Issues](https://github.com/FizaAslam1/customer-churn-prediction/issues)
- Provide detailed description and steps to reproduce
- Include screenshots or error messages

---

## 📄 License

This project is open source and available for educational and commercial use. See LICENSE file for details.

---

## 👩‍💻 About the Developer

**Fiza Aslam**  
Data Science Enthusiast | BS IT Student  
The Islamia University of Bahawalpur, Pakistan

**Connect with me:**
- 💼 [LinkedIn](https://www.linkedin.com/in/fiza-aslam-07a3863a4)
- 🔗 [GitHub](https://github.com/FizaAslam1)
- 📊 [Kaggle](https://www.kaggle.com/fizaaslam12)

---

**Last Updated:** June 2026
**Repository Status:** ✅ Actively Maintained
