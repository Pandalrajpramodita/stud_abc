import streamlit as st
import requests

st.title("👔 Score Predictor 📕")

study = st.slider("Study Time", 0, 10)
atd = st.slider("Attended Days", 0, 80)
gen = st.selectbox("Gender", ["Male", "Female"])

# Fixing the gender logic
gender = 1 if gen == "Male" else 0

if st.button("Predict the score"):
    data = {
        "study_time": study,
        "attendence": atd,
        "gender_Male": gender
    }

    # Fixed URL (removed space)
    res = requests.post("https://fastapi-ij23.onrender.com/predict", json=data)
    result = res.json()

    st.write("The Predicted Score is:", result["Predicted_score"])
    
