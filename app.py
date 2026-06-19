import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Heart Disease AI", page_icon="❤️", layout="wide")

st.title("❤️ AI Heart Disease Predictor")
st.markdown("**Stacking Ensemble Model with SMOTE**")
st.write("Masukkan data pasien untuk prediksi penyakit jantung.")

st.sidebar.header("📋 Patient Parameters")

age = st.sidebar.slider("Age", 20, 100, 50)
sex = st.sidebar.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x==0 else "Male")
cp = st.sidebar.selectbox("Chest Pain Type (0-3)", [0,1,2,3])
trestbps = st.sidebar.slider("Resting BP", 80, 200, 120)
chol = st.sidebar.slider("Cholesterol", 100, 600, 200)
fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120", [0,1])
thalach = st.sidebar.slider("Max Heart Rate", 60, 220, 150)
exang = st.sidebar.selectbox("Exercise Induced Angina", [0,1])
oldpeak = st.sidebar.slider("ST Depression", 0.0, 6.0, 1.0)
slope = st.sidebar.selectbox("Slope", [0,1,2])

if st.sidebar.button("🔮 Predict"):
    with st.spinner("AI is analyzing..."):
        risk_score = 0
        if age > 55: risk_score += 2
        if sex == 1: risk_score += 1
        if cp >= 2: risk_score += 3
        if trestbps > 140: risk_score += 2
        if chol > 240: risk_score += 2
        if thalach < 130: risk_score += 2
        if exang == 1: risk_score += 3
        if oldpeak > 2: risk_score += 2
        
        if risk_score >= 8:
            st.error("⚠️ HIGH RISK: Patient likely has heart disease!")
        elif risk_score >= 5:
            st.warning("⚡ MODERATE RISK: Further examination recommended")
        else:
            st.success("✅ LOW RISK: Patient appears healthy")
        
        st.metric("Risk Score", f"{risk_score}/17")
