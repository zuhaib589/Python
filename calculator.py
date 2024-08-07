import streamlit as st

def main():
    st.title("Simple Calculator")
    
    # Input fields for numbers
    num1 = st.number_input("Enter the first number", format="%f")
    num2 = st.number_input("Enter the second number", format="%f")

    # Dropdown for selecting the operation
    operation = st.selectbox("Select Operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Calculate result based on operation
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is undefined.")
            return

    # Display result
    st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
