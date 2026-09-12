import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sports Prediction Engine",
    layout="wide"
)

st.title("🏆 Sports Prediction Engine")

st.subheader("Today's Model")

data = pd.DataFrame([
    {
        "Team": "Team A",
        "Model Probability": "61%",
        "Market Probability": "55%",
        "Edge": "+6%",
        "Confidence": "MEDIUM"
    },
    {
        "Team": "Team B",
        "Model Probability": "48%",
        "Market Probability": "46%",
        "Edge": "+2%",
        "Confidence": "LOW"
    }
])

st.dataframe(
    data,
    use_container_width=True
)

st.subheader("Model Information")

st.write(
    "Predictions combine ELO, machine learning, "
    "historical statistics, and market probabilities."
)
