import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="AI-Powered Project Risk AnalysisDashboard", layout="wide")

st.title("AI-Powered Construction Project Risk Analysis Dashboard")

# Sidebar inputs
st.sidebar.header("Enter Project Details")

budget = st.sidebar.number_input("Budget", min_value=100000.0, value=5000000.0)
duration = st.sidebar.number_input("Duration (days)", min_value=1, value=120)
workers = st.sidebar.number_input("Number of Workers", min_value=1, value=30)
material_delay = st.sidebar.slider("Material Delay Risk", 0.0, 1.0, 0.5)
weather_risk = st.sidebar.slider("Weather Risk", 0.0, 1.0, 0.5)
previous_delays = st.sidebar.number_input("Previous Delays", min_value=0, value=0)

if st.sidebar.button("Predict Risk"):

    payload = {
        "budget": budget,
        "duration": duration,
        "workers": workers,
        "material_delay": material_delay,
        "weather_risk": weather_risk,
        "previous_delays": previous_delays
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()

        st.subheader("Risk Predictions Results")

        col1, col2, col3 = st.columns(3)

        col1.metric("Delay Probability", f"{result['delay_probability']}")
        col2.metric("Cost Overrun Probability", f"{result['cost_overrun_probability']}")
        col3.metric("Overall Risk", result['overall_risk'])

        # Chart
        fig, ax = plt.subplots()
        ax.bar(
            ["Delay", "Cost Overrun"],
            [result["delay_probability"], result["cost_overrun_probability"]]
        )
        ax.set_ylim(0, 1)
        ax.set_ylabel("Probability")
        st.pyplot(fig)

    else:
        st.error("API Error. Make sure FastAPI is running.")
