import streamlit as st

# Initialize our Streamlit app
st.set_page_config(page_title="Addition Tutor")

st.header("Learn to Add with AI")

# Initialize session state for tracking attempts
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# Input fields for numbers side by side
col1, col2 = st.columns(2)
with col1:
    number1 = st.number_input("First number:", format="%f", key="num1")
with col2:
    number2 = st.number_input("Second number:", format="%f", key="num2")

# Convert float inputs to integers
number1 = int(number1)
number2 = int(number2)

# Input for user's answer
user_answer = st.number_input("What is the sum of these numbers?", key="user_ans")

# Button to submit the answer
submit = st.button("Check my answer")

# Function to generate examples based on attempts
def generate_example(num1, num2, attempt):
    examples = [
        f"Imagine you have {num1} apples and you find {num2} more apples. How many apples do you have in total?",
        f"Think of it as adding {num1} stars to a night sky that already has {num2} stars. How bright is the sky now?",
        f"You're on a treasure hunt and find {num1} gold coins, then {num2} more. How rich are you now?"
    ]
    return examples[attempt % len(examples)]

# Respond to the button click
if submit:
    correct_answer = number1 + number2
    if user_answer == correct_answer:
        st.write("Congratulations! You got it right! 🎉 Keep up the good work and try more questions to practice!")
        st.session_state.attempts = 0  # Reset attempts after a correct answer
    else:
        st.session_state.attempts += 1
        if st.session_state.attempts == 1:
            st.write("Oops! It seems like you might need some help with this. Let's try a different approach.")
        else:
            st.write("Still not quite right. Let’s try another example.")
        
        example = generate_example(number1, number2, st.session_state.attempts - 1)
        st.write("Here's an example to help you:")
        st.write(example)
