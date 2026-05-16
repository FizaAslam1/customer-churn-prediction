import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Page config
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Telecom Customer Churn Prediction")
st.markdown("### Predict if a customer will leave or stay")

# Load model files
@st.cache_resource
def load_models():
    try:
        model = joblib.load('churn_model.pkl')
        scaler = joblib.load('scaler.pkl')
        features = joblib.load('feature_names.pkl')
        return model, scaler, features
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None, None

model, scaler, features = load_models()

if model is None:
    st.stop()

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Customer Information")
    
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    
    st.subheader("📞 Phone Services")
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    
    st.subheader("🌐 Internet Service")
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

with col2:
    st.subheader("🔒 Security & Support")
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    
    st.subheader("📺 Streaming Services")
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    
    st.subheader("💰 Billing & Contract")
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (auto)", "Credit card (auto)"])
    
    st.subheader("💵 Charges")
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 150.0, 70.0)
    total_charges = st.number_input("Total Charges ($)", 0.0, 9000.0, 500.0)

# Predict button
if st.button("🔮 Predict Churn Risk", type="primary", use_container_width=True):
    
    # Prepare input data
    input_data = {
        'gender': 1 if gender == "Male" else 0,
        'SeniorCitizen': 1 if senior_citizen == "Yes" else 0,
        'Partner': 1 if partner == "Yes" else 0,
        'Dependents': 1 if dependents == "Yes" else 0,
        'tenure': tenure,
        'PhoneService': 1 if phone_service == "Yes" else 0,
        'MultipleLines_No': 1 if multiple_lines == "No" else 0,
        'MultipleLines_No phone service': 1 if multiple_lines == "No phone service" else 0,
        'MultipleLines_Yes': 1 if multiple_lines == "Yes" else 0,
        'InternetService_Fiber optic': 1 if internet_service == "Fiber optic" else 0,
        'InternetService_No': 1 if internet_service == "No" else 0,
        'OnlineSecurity_No': 1 if online_security == "No" else 0,
        'OnlineSecurity_No internet service': 1 if online_security == "No internet service" else 0,
        'OnlineSecurity_Yes': 1 if online_security == "Yes" else 0,
        'OnlineBackup_No': 1 if online_backup == "No" else 0,
        'OnlineBackup_No internet service': 1 if online_backup == "No internet service" else 0,
        'OnlineBackup_Yes': 1 if online_backup == "Yes" else 0,
        'DeviceProtection_No': 1 if device_protection == "No" else 0,
        'DeviceProtection_No internet service': 1 if device_protection == "No internet service" else 0,
        'DeviceProtection_Yes': 1 if device_protection == "Yes" else 0,
        'TechSupport_No': 1 if tech_support == "No" else 0,
        'TechSupport_No internet service': 1 if tech_support == "No internet service" else 0,
        'TechSupport_Yes': 1 if tech_support == "Yes" else 0,
        'StreamingTV_No': 1 if streaming_tv == "No" else 0,
        'StreamingTV_No internet service': 1 if streaming_tv == "No internet service" else 0,
        'StreamingTV_Yes': 1 if streaming_tv == "Yes" else 0,
        'StreamingMovies_No': 1 if streaming_movies == "No" else 0,
        'StreamingMovies_No internet service': 1 if streaming_movies == "No internet service" else 0,
        'StreamingMovies_Yes': 1 if streaming_movies == "Yes" else 0,
        'Contract_One year': 1 if contract == "One year" else 0,
        'Contract_Two year': 1 if contract == "Two year" else 0,
        'PaperlessBilling': 1 if paperless_billing == "Yes" else 0,
        'PaymentMethod_Bank transfer (auto)': 1 if payment_method == "Bank transfer (auto)" else 0,
        'PaymentMethod_Credit card (auto)': 1 if payment_method == "Credit card (auto)" else 0,
        'PaymentMethod_Electronic check': 1 if payment_method == "Electronic check" else 0,
        'PaymentMethod_Mailed check': 1 if payment_method == "Mailed check" else 0,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }
    
    # Create DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Add missing columns
    for col in features:
        if col not in input_df.columns:
            input_df[col] = 0
    
    input_df = input_df[features]
    
    # Scale numeric columns
    numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])
    
    # Predict
    prob = model.predict_proba(input_df)[0, 1]
    pred = "Churn" if prob > 0.5 else "No Churn"
    
    # Display results
    st.markdown("---")
    st.subheader("📈 Prediction Result")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.metric("Churn Probability", f"{prob:.1%}")
    
    with col_b:
        if pred == "Churn":
            st.error("⚠️ Customer WILL Churn")
        else:
            st.success("✅ Customer will NOT Churn")
    
    with col_c:
        if prob > 0.7:
            st.warning("🔴 High Risk")
        elif prob > 0.4:
            st.warning("🟡 Medium Risk")
        else:
            st.info("🟢 Low Risk")
    
    # Recommendation
    st.markdown("---")
    st.subheader("💡 Recommendation")
    
    if prob > 0.7:
        st.error("🚨 **Urgent Action Required!** Offer 20% discount + free upgrade immediately")
    elif prob > 0.4:
        st.warning("📧 **Send retention email** with 10% discount offer")
    else:
        st.success("✅ **Customer is loyal.** No action needed")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Customer Churn Prediction Model (78% Accuracy)")