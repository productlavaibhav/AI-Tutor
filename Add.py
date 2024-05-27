import streamlit as st
import random

# Set up page configuration
st.set_page_config(page_title="Interactive Math Tutor")

st.header("Interactive Math Tutor")

# Initialize session variables if they don't exist
if 'initialized' not in st.session_state:
    st.session_state['initialized'] = False
    st.session_state['name'] = ""
    st.session_state['operation'] = None
    st.session_state['attempts'] = 0
    st.session_state['previous_difference'] = float('inf')

def get_example(num1, num2, operation):
    if operation == 'add':
        action = "adding"
    else:
        action = "subtracting"
    examples = [
        f"Imagine you have {num1} apples and you're {action} {num2}.",
        f"If you were stacking {num1} books and {action} {num2} more books, how many would you have?",
        f"Picture having {num1} pencils, and you {action} {num2} more. Total pencils?"
    ]
    return random.choice(examples)

def handle_response(num1, num2, user_answer, operation):
    operations = {
        "add": num1 + num2,
        "subtract": num1 - num2
    }
    correct_answer = operations[operation]
    difference = abs(user_answer - correct_answer)
    response = ""
    
    if user_answer == correct_answer:
        response = "That's correct! 🎉 Great job!"
        st.session_state.attempts = 0
    else:
        if st.session_state.attempts > 0 and difference < st.session_state.previous_difference:
            response = "You're getting closer! 😊 Try again, you can do it!"
        else:
            response = "That’s not quite right. 😕 Here’s an example to help you understand:"
        
        example = get_example(num1, num2, operation)
        response += f" {example}"
        st.session_state.attempts += 1
        st.session_state.previous_difference = difference

    return response

# Step 1: Ask for the user's name
if 'name' not in st.session_state or not st.session_state['name']:
    st.session_state['name'] = st.text_input("What's your name?", key="name_input")

# Step 2: Ask how they are doing
if st.session_state['name'] and not st.session_state.initialized:
    response = st.text_input(f"Hello, {st.session_state['name']}! How are you doing today?", key="emotion_input")
    if response:
        st.session_state.initialized = True
        emotional_reply = "Thank you for sharing. 😌 Let's get started with some math!"
        st.write(emotional_reply)

# Step 4: Ask what operation they want to perform
if st.session_state.initialized:
    operation = st.radio("What do you want to do?", ('add', 'subtract'), key="operation_select")

    # Step 5: Show the fields for input numbers and response
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number:", format="%d", key="num1")
    with col2:
        num2 = st.number_input("Enter second number:", format="%d", key="num2")
    
    user_answer = st.number_input("What is the result?", format="%d", key="user_ans")
    submit = st.button("Check my answer", key="submit")

    # Step 6: Handle the response based on user's answer
    if submit and operation:
        response = handle_response(num1, num2, user_answer, operation)
        st.write(response)
