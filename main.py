import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('new.pkl', 'rb'))

# Streamlit application
st.title("Weather Prediction")

# Form to input weather data
with st.form(key='weather_form'):
    precipitation = st.text_input("Precipitation")
    temp_max = st.text_input("Max Temperature (°C)")
    temp_min = st.text_input("Min Temperature (°C)")
    wind = st.text_input("Wind")
    year = st.text_input("Year")
    month = st.text_input("Month")
    
    submit_button = st.form_submit_button(label='Predict')

if submit_button:
    try:
        # Prepare input data for prediction
        input_data = np.array([float(precipitation), float(temp_max), float(temp_min), float(wind), int(year), int(month)]).reshape(1, 6)
        
        # Make prediction using loaded model
        result = model.predict(input_data)[0]
        
        # Define weather conditions
        weather_conditions = {0: 'Drizzle', 1: 'Fog', 2: 'Rainy', 3: 'Snow', 4: 'Sunny'}
        result_text = weather_conditions.get(result, "Unknown")
        
        st.success(f"Predicted Weather is {result_text}!")
    except Exception as e:
        st.error(f"Error: {e}")
