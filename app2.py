import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(page_title="Student Score Predictor", page_icon="📊")

st.title("📊 Student Score Predictor")
st.write("Predict exam score based on hours studied")

# Load model
with open("student_score_model.pkl", "rb") as f:
    model = pickle.load(f)

# Input
hours = st.number_input(
    "Hours Studied",
    min_value=0.0,
    max_value=24.0,
    step=0.5
)

# Prediction
if st.button("Predict Score"):
    input_df = pd.DataFrame({"hours_studied": [hours]})
    prediction = model.predict(input_df)[0]
    st.success(f"📈 Predicted Score: {round(prediction)}")
