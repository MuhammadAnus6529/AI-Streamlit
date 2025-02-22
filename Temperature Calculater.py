import streamlit as st

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius (°C)" and to_unit == "Fahrenheit (°F)":
        return (value * 9/5) + 32
    elif from_unit == "Celsius (°C)" and to_unit == "Kelvin (K)":
        return value + 273.15
    elif from_unit == "Fahrenheit (°F)" and to_unit == "Celsius (°C)":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit (°F)" and to_unit == "Kelvin (K)":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin (K)" and to_unit == "Celsius (°C)":
        return value - 273.15
    elif from_unit == "Kelvin (K)" and to_unit == "Fahrenheit (°F)":
        return (value - 273.15) * 9/5 + 32

st.set_page_config(page_title="🌡️ Temperature Converter", layout="centered")

st.markdown(
    """
    <style>
        body {
            background: white;
            color: white;
            text-align: center;
        }
        .stApp {
            background-color: rgba(0, 0, 0, 0.1);
            padding: 2rem;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>🌡️ Temperature Converter</h1>", unsafe_allow_html=True)

temp = st.number_input("Enter Temperature:", value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit:", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])
to_unit = st.selectbox("To Unit:", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])

if st.button("Convert Temperature"):
    converted_temp = convert_temperature(temp, from_unit, to_unit)
    st.success(f"{temp:.2f} {from_unit} is equal to {converted_temp:.2f} {to_unit}")
