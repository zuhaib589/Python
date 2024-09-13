import streamlit as st

# Function to determine the quadrant of a point
def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant 1"
    elif x < 0 and y > 0:
        return "Quadrant 2"
    elif x < 0 and y < 0:
        return "Quadrant 3"
    elif x > 0 and y < 0:
        return "Quadrant 4"
    elif x == 0 and y != 0:
        return "On the Y-axis"
    elif y == 0 and x != 0:
        return "On the X-axis"
    else:
        return "Origin"

# Streamlit UI
st.title("Quadrant Finder")
st.write("Enter the coordinates of the point (x, y) to find which quadrant it lies in.")

# Input fields for x and y coordinates
x = st.number_input("Enter x-coordinate", value=0.0)
y = st.number_input("Enter y-coordinate", value=0.0)

# Button to submit the inputs
if st.button("Find Quadrant"):
    quadrant = find_quadrant(x, y)
    st.write(f"The point ({x}, {y}) lies in: {quadrant}")
