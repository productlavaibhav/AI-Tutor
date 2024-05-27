import streamlit as st
import random

# Set up page configuration
st.set_page_config(page_title="Addition Tutor AI")

st.header("Learn to Add with AI")

# Initialize session variables if they don't exist
if 'name' not in st.session_state:
    st.session_state['name'] = None
    st.session_state['num1'] = None
    st.session_state['num2'] = None
    st.session_state['user_answer'] = None
    st.session_state['attempts'] = 0
    st.session_state['previous_difference'] = float('inf')

def get_example(num1, num2):
    scenarios = [
        f"Imagine you have {num1} apples and find {num2} more.",
        f"If you were stacking {num1} books and got {num2} more books, how many would you have?",
        f"Picture having {num1} pencils, and you buy {num2} more. Total pencils?"
    ]
    return random.choice(scenarios)

def handle_response(num1, num2, user_answer):
    correct_answer = num1 + num2
    difference = abs(user_answer - correct_answer)
    closer = difference < st.session_state['previous_difference']
    response = ""
    
    if user_answer == correct_answer:
        response = "That's correct! 🎉 Great job! Try changing the numbers to practice more."
        st.session_state['attempts'] = 0
        st.session_state['previous_difference'] = float('inf')
    else:
        if st.session_state['attempts'] > 0:
            if closer:
                response = "You're getting closer! Try again, you can do it!"
            else:
                response = "That's not quite right. Let's try another approach."
        else:
            response = "That’s not correct. Here’s an example to help you understand:"
        
        example = get_example(num1, num2)
        response += f" {example}"
        st.session_state['attempts'] += 1
        st.session_state['previous_difference'] = difference

    return response

if 'name' not in st.session_state or st.session_state['name'] is None:
    st.session_state['name'] = st.text_input("What's your name?")

if st.session_state['name']:
    st.write(f"Hello, {st.session_state['name']}! How are you doing today?")
    
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number:", format="%d", key="num1")
    with col2:
        num2 = st.number_input("Enter second number:", format="%d", key="num2")
    
    user_answer = st.number_input("What is the sum of these numbers?", format="%d", key="user_ans")
    submit = st.button("Submit")
    
    if submit:
        response = handle_response(num1, num2, user_answer)
        st.write(response)
