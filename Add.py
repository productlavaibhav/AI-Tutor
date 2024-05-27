import streamlit as st

# Initialize our Streamlit app
st.set_page_config(page_title="Addition Tutor")

st.header("Learn to Add with AI")

# Initialize session state for tracking attempts and previous differences
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
    st.session_state.previous_difference = float('inf')

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

# Function to generate examples based on how off the mark the user is
def generate_example(num1, num2, difference):
    if difference > 10:
        return f"Let's think big! If you have {num1} toy cars and your friend gives you {num2} more, how many do you have? Start from {num1} and count up {num2} more."
    elif difference > 5:
        return f"Imagine you're helping to set up {num1} chairs, and then {num2} more chairs arrive. Count out loud from {num1} up to {num1 + num2} to see how many chairs there are in total."
    else:
        return f"You're very close! You're stacking blocks. You already have {num1} blocks and add {num2} more. Try to stack them one by one to see the total."

# Respond to the button click
if submit:
    correct_answer = number1 + number2
    difference = abs(user_answer - correct_answer)
    
    if user_answer == correct_answer:
        st.write("Congratulations! You got it right! 🎉 Keep up the good work and try more questions to practice!")
        st.session_state.attempts = 0  # Reset attempts after a correct answer
        st.session_state.previous_difference = float('inf')
    else:
        if difference < st.session_state.previous_difference:
            st.write("You're on the right track! You're getting closer!")
        else:
            st.write("That's not quite right. Let's try another approach.")

        example = generate_example(number1, number2, difference)
        st.write("Here's an example to help you:")
        st.write(example)
        st.session_state.attempts += 1
        st.session_state.previous_difference = difference
