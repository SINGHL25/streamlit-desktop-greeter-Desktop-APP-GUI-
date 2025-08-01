import streamlit as st

st.set_page_config(page_title="Desktop App Greeter", layout="centered")

st.title("👋 Streamlit Desktop-Like App")

name = st.text_input("Enter your name:")

if st.button("Greet Me"):
    if name.strip():
        st.success(f"Hello, {name}!")
    else:
        st.warning("Please enter a name first.")

