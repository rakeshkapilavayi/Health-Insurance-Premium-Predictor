import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Health Insurance Premium Predictor", layout="wide")

st.markdown(
    "<h2 style='text-align: center; color: #FF6600;'>🏥 Health Insurance Premium Predictor</h2><hr>",
    unsafe_allow_html=True
)

with st.expander("📋 Personal Information", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider("🎂 Age", 18, 100, 30, help="Select your age (between 18 and 100).")
    with col2:
        gender = st.radio("🧑 Gender", ['Male', 'Female'], help="Biological gender for policy assessment.")
    with col3:
        marital_status = st.radio("💍 Marital Status", ['Unmarried', 'Married'], help="Marital status impacts family coverage.")

with st.expander("👨‍👩‍👧 Family & Lifestyle"):
    col1, col2, col3 = st.columns(3)
    with col1:
        number_of_dependants = st.slider("👶 Number of Dependants", 0, 20, 1, help="How many people depend on your income?")
    with col2:
        smoking_status = st.selectbox("🚬 Smoking Habit", ['No Smoking', 'Regular', 'Occasional'], help="Your smoking frequency.")
    with col3:
        bmi_category = st.selectbox("⚖️ BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'], help="Your current BMI classification.")

with st.expander("💼 Employment & Income"):
    col1, col2, col3 = st.columns(3)
    with col1:
        employment_status = st.selectbox("💼 Employment Type", ['Salaried', 'Self-Employed', 'Freelancer', ''], help="Your primary source of income.")
    with col2:
        income_lakhs = st.slider("💰 Income (in Lakhs)", 0, 200, 10, help="Your annual income in INR lakhs.")
    with col3:
        region = st.selectbox("📍 Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'], help="Your geographic region of residence.")

with st.expander("🏥 Medical & Insurance Info"):
    col1, col2, col3 = st.columns(3)
    with col1:
        medical_history = st.selectbox("🩺 Medical History", [
            'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
            'Thyroid', 'Heart disease', 'High blood pressure & Heart disease',
            'Diabetes & Thyroid', 'Diabetes & Heart disease'
        ], help="Any known past or present medical conditions?")
    with col2:
        insurance_plan = st.radio("🛡️ Insurance Plan", ['Bronze', 'Silver', 'Gold'], help="Select your insurance plan level.")
    with col3:
        genetical_risk = st.slider("🧬 Genetic Risk", 0, 5, 1, help="Any family history of diseases? Rate the severity from 0 to 5.")

# Combine inputs into a dict
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Predict Button
if st.button("🚀 Predict Insurance Premium"):
    prediction = predict(input_dict)
    st.success(f"💸 Predicted Health Insurance Cost: ₹{prediction}")
