import streamlit as st
import random

# Set up page configuration
st.set_page_config(page_title="Addition Tutor AI")

st.header("Learn to Add with AI")

# Initialize session variables if they don't exist
if 'initialized' not in st.session_state:
    st.session_state['initialized'] = False
    st.session_state['name'] = ""
    st.session_state['attempts'] = 0
    st.session_state['previous_difference'] = float('inf')
    st.session_state['chat_history'] = []

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

# Function to respond emotionally to user input
def respond_emotionally(user_input):
    responses = {
        "good": "That's great to hear! 😊",
        "well": "I'm glad you're doing well! 👍",
        "okay": "Okay, let's get started then! 😄",
        "not good": "Oh, I'm sorry to hear that. 😔",
        "bad": "I hope things get better soon. 🙏"
    }
    for keyword in responses:
        if keyword in user_input.lower():
            return responses[keyword]
    return "I understand. Let's get started! 🚀"

# Ask for the user's name if not already provided
if not st.session_state['initialized']:
    name = st.text_input("What's your name?", key="name_input")
    if st.button("Enter", key="enter_name"):
        st.session_state['name'] = name
        st.session_state['initialized'] = True

if st.session_state['initialized']:
    st.write(f"Hello, {st.session_state['name']}! How are you doing today?")

    # Get user input and respond emotionally
    user_response = st.text_input("Tell me how you are doing:", key="user_response")
    if user_response:
        st.session_state['chat_history'].append(f"You: {user_response}")
        st.write(respond_emotionally(user_response))
        st.session_state['chat_history'].append(f"AI: {respond_emotionally(user_response)}")
        for msg in st.session_state['chat_history']:
            st.write(msg)
        
    st.write("What would you like to do? ")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input("Enter first number:", format="%d", key="num1")
    with col2:
        operation = st.selectbox("Choose an operation", ["+", "-"], key="operation")
    with col3:
        num2 = st.number_input("Enter second number:", format="%d", key="num2")

    user_answer = st.number_input("What is the result?", format="%d", key="user_ans")
    submit = st.button("Submit")
    
    if submit:
        if operation == "+":
            response = handle_response(num1, num2, user_answer)
        else:
            response = handle_response(num1, -num2, user_answer)  # Handle subtraction
        st.write(response)
