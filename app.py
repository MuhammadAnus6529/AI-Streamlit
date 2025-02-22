import streamlit as st
import datetime

def age_calculator():
    st.title("🎂 Age Calculator")

    birth_date = st.date_input("Select your birth date:")
    
    if birth_date:
        today = datetime.date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        st.success(f"🎉 You are {age} years old.")

if __name__ == "__main__":
    age_calculator()
