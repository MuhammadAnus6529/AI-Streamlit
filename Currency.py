import streamlit as st

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency == to_currency:
        return amount
    return amount * exchange_rates.get((from_currency, to_currency), 1)

st.set_page_config(page_title="💱 Currency Converter", layout="centered")

st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #ff7e5f, #feb47b);
            color: white;
            text-align: center;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.2);
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #ff5733;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #c70039;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>💱 Currency Converter</h1>", unsafe_allow_html=True)

currencies = {"USD": "United States Dollar", "EUR": "Euro", "GBP": "British Pound Sterling", "PKR": "Pakistani Rupee"}
exchange_rates = {("USD", "EUR"): 0.91, ("USD", "GBP"): 0.76, ("USD", "PKR"): 277.50,
                  ("EUR", "USD"): 1.10, ("EUR", "GBP"): 0.84, ("EUR", "PKR"): 304.25,
                  ("GBP", "USD"): 1.32, ("GBP", "EUR"): 1.19, ("GBP", "PKR"): 362.75,
                  ("PKR", "USD"): 0.0036, ("PKR", "EUR"): 0.0033, ("PKR", "GBP"): 0.0028}

amount = st.number_input("Enter Amount:", value=1.0, min_value=0.0, format="%.2f")
from_currency = st.selectbox("From Currency:", list(currencies.keys()))
to_currency = st.selectbox("To Currency:", list(currencies.keys()))

if st.button("Convert Currency"):
    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
    st.success(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
