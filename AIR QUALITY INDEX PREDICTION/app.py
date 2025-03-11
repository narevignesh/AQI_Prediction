import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained model and scalers
with open('AIR_QUALITY_INDEX.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('X_scaler.pkl', 'rb') as x_scaler_file:
    X_scaler = pickle.load(x_scaler_file)
with open('y_scaler.pkl', 'rb') as y_scaler_file:
    y_scaler = pickle.load(y_scaler_file)

st.set_page_config(page_title="Air Quality Prediction", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #D4FC79, #96E6A1);
            padding: 20px;
        }
        h1 {
            color: #2C3E50;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        .stButton > button {
            background: linear-gradient(45deg, #FF7675, #D63031);
            color: black !important;
            font-size: 18px;
            padding: 12px 25px;
            border-radius: 8px;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            transform: scale(1.05);
        }
        .results-box {
            border-radius: 15px;
            padding: 25px;
            margin-top: 25px;
            text-align: center;
            color: #ffffff;
            font-size: 20px;
            font-weight: bold;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            background: linear-gradient(to right, #A1C4FD, #C2E9FB);
        }
        .awareness-box {
            background: #ffffff;
            border-radius: 12px;
            padding: 20px;
            margin-top: 30px;
            text-align: left;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            color: #2C3E50;
            font-size: 18px;
            font-weight: 500;
        }
        .awareness-box h2 {
            text-align: center;
            color: #27AE60;
            font-size: 24px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🌍 Air Quality Index (AQI) Prediction ")
st.write("Enter the air quality parameters below to predict AQI and assess air quality levels.")

param_names = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'SO2', 'NH3', 'CO', 'O3', 'Benzene', 'Toluene', 'Xylene']
user_inputs = []

col1, col2 = st.columns(2)

for i, param in enumerate(param_names):
    with col1 if i % 2 == 0 else col2:
        value = st.number_input(f"{param} (µg/m³)", min_value=0.0, step=0.1, format="%.2f")
        user_inputs.append(value)

if st.button("🔍 Predict AQI"):
    input_data = np.array(user_inputs).reshape(1, -1)
    input_scaled = X_scaler.transform(input_data)
    aqi_scaled = model.predict(input_scaled)
    aqi = y_scaler.inverse_transform(aqi_scaled.reshape(-1, 1))[0][0]
    
    if aqi <= 50:
        color = "#00C853"
        status = "✅ Good Air Quality (Minimal impact)"
        emoji = "🌿"
    elif aqi <= 100:
        color = "#FFD600"
        status = "🟡 Moderate Air Quality (Sensitive groups at risk)"
        emoji = "🌤️"
    elif aqi <= 150:
        color = "#FFAB00"
        status = "🟠 Unhealthy for Sensitive Groups"
        emoji = "😷"
    elif aqi <= 200:
        color = "#D50000"
        status = "🔴 Unhealthy (Reduce outdoor activity)"
        emoji = "🚨"
    elif aqi <= 300:
        color = "#6A1B9A"
        status = "🟣 Very Unhealthy (Health alert)"
        emoji = "☠️"
    else:
        color = "#263238"
        status = "⚫ Hazardous (Stay indoors, emergency!)"
        emoji = "🏴"
    
    st.markdown(
        f'<div class="results-box" style="border: 2px solid {color};">'
        f'<h3>{emoji} Predicted AQI: {aqi:.2f}</h3>'
        f'<p>{status}</p>'
        '</div>',
        unsafe_allow_html=True
    )

st.markdown(
        """
        <div class="awareness-box">
            <h2>🌿 Why is Air Quality Important? 💨</h2>
            <p>🌍 Poor air quality affects both the environment and human health.</p>
            <p>😷 High AQI levels can cause respiratory diseases, allergies, and lung infections.</p>
            <p>🧒 Children, elderly, and individuals with asthma are more vulnerable to air pollution.</p>
            <p>🚗 Major pollutants come from vehicles, industries, and burning fossil fuels.</p>
            <p>🌱 Planting more trees and reducing vehicle emissions can help improve air quality.</p>
            <p>🏡 Staying indoors on high AQI days can reduce exposure to harmful pollutants.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.markdown("<p style='text-align:center;font-size:16px;color:#2C3E50;'>🌱 Breathe fresh, live healthy! Developed by NARE VIGNESH 🚀</p>", unsafe_allow_html=True)