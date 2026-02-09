import streamlit as st

st.title("Calculator")

num1 = st.number_input("Number 1", value=0.0)
num2 = st.number_input("Number 2", value=0.0)

operation = st.selectbox(
    "Select calculation",
    ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"]
)

if st.button("calculate"):
    if operation == "Add (+)":
        result = num1 + num2
    elif operation == "Subtract (-)":
        result = num1 - num2
    elif operation == "Multiply (×)":
        result = num1 * num2
    elif operation == "Divide (÷)":
        if num2 == 0:
            st.error("Do not divide by zero.")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"Result = {result}")
