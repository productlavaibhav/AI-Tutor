import streamlit as st
import random

# Initialize our Streamlit app
st.set_page_config(page_title="Addition Tutor")

st.header("Learn to Add with AI")

# Input fields for numbers side by side
col1, col2 = st.columns(2)
with col1:
    number1 = st.number_input("First number:", format="%f")
with col2:
    number2 = st.number_input("Second number:", format="%f")

# Convert float inputs to integers
number1 = int(number1)
number2 = int(number2)

# Input for user's answer
user_answer = st.number_input("What is the sum of these numbers?")

# Button to submit the answer
submit = st.button("Check my answer")

# Define correct and incorrect responses
correct_response = "Congratulations! You got it right! 🎉 Keep up the good work and practice more!"
incorrect_response = "Oops! It seems like you might need some help with this. Let's try a different approach."

# Function to generate random example
def generate_example(num1, num2):
    example = f"Imagine you have {num1} apples and you find {num2} more apples. How many apples do you have in total?"
    return example

# Respond to the button click
if submit:
    if user_answer == number1 + number2:
        st.write(correct_response)
    else:
        st.write(incorrect_response)
        example = generate_example(number1, number2)
        st.write("Here's an example to help you:")
        st.write(example)
