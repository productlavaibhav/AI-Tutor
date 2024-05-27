import streamlit as st
import random

# Set up page configuration
st.set_page_config(page_title="Addition Tutor AI")

# Initialize session variables
if 'state' not in st.session_state:
    st.session_state.state = 'intro'
    st.session_state.attempts = 0
    st.session_state.previous_difference = float('inf')

def get_example(num1, num2):
    # Generating a random example based on simple scenarios
    scenarios = [
        f"Imagine you have {num1} apples and find {num2} more.",
        f"If you were stacking {num1} books and got {num2} more books, how many would you have?",
        f"Picture having {num1} pencils, and you buy {num2} more. Total pencils?",
        # Add more scenarios up to 15 or more
    ]
    return random.choice(scenarios)

def handle_response(user_answer, num1, num2):
    correct_answer = num1 + num2
    difference = abs(user_answer - correct_answer)
    closer = difference < st.session_state.previous_difference
    response = ""
    
    if user_answer == correct_answer:
        response = "That's correct! 🎉 Great job! Try changing the numbers to practice more."
        st.session_state.state = 'completed'
    else:
        if st.session_state.attempts > 0:
            if closer:
                response = "You're getting closer! Try again, you can do it!"
            else:
                response = "That's not quite right. Let's try another approach."
        else:
            response = "That’s not correct. Here’s an example to help you understand:"
        
        example = get_example(num1, num2)
        response += f" {example}"
        st.session_state.attempts += 1
        st.session_state.previous_difference = difference

    return response

def main_conversation():
    st.title("Welcome to the Addition Tutor AI!")
    
    if st.session_state.state == 'intro':
        name = st.text_input("What's your name?")
        if name:
            st.session_state.state = 'greeting'
            st.session_state.name = name

    if st.session_state.state == 'greeting':
        st.write(f"Hello, {st.session_state.name}! How are you doing today?")
        st.session_state.state = 'problem_setup'
    
    if st.session_state.state == 'problem_setup':
        st.write("Let's start with an addition problem.")
        st.session_state.state = 'collect_numbers'

    if st.session_state.state == 'collect_numbers':
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.num1 = st.number_input("Enter first number:", key="num1")
        with col2:
            st.session_state.num2 = st.number_input("Enter second number:", key="num2")
        
        user_answer = st.number_input("What is the sum of these numbers?", key="user_answer")
        if st.button("Submit"):
            response = handle_response(user_answer, st.session_state.num1, st.session_state.num2)
            st.write(response)

if __name__ == '__main__':
    main_conversation()
