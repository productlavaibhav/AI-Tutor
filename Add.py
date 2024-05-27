import streamlit as st
import random

# Set up page configuration
st.set_page_config(page_title="Interactive Math Tutor")

st.header("Interactive Math Tutor")

# Initialize session variables if they don't exist
if 'initialized' not in st.session_state:
    st.session_state.initialized = False
    st.session_state.name = ""
    st.session_state.operation = None
    st.session_state.emotional_response = None

def get_example(num1, num2, operation):
    examples = [
        f"Imagine you have {num1} apples and {operation} {num2} more.",
        f"If you were stacking {num1} books and {operation} {num2} more books, how many would you have?",
        f"Picture having {num1} pencils, and you {operation} {num2} more. Total pencils?"
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
        response = "That’s not quite right. Here’s an example to help you understand:"
        example = get_example(num1, num2, "add" if operation == "add" else "subtract")
        response += f" {example}"
        st.session_state.attempts += 1

    return response

# Name input and emotional interaction
if not st.session_state.initialized:
    name = st.text_input("What's your name?", key="name_input")
    if st.button("Enter", key="enter_name"):
        st.session_state.name = name
        st.session_state.initialized = True
        st.session_state.state = 'emotion'

if st.session_state.initialized and 'state' in st.session_state and st.session_state.state == 'emotion':
    st.write(f"Hello, {st.session_state.name}! How are you doing today?")
    emotional_response = st.text_input("I'm here to listen:", key="emotion_input")
    if st.button("Submit Emotion", key="emotion_submit"):
        st.session_state.emotional_response = emotional_response
        st.session_state.state = 'operation'
        st.write("Thank you for sharing. Let's continue!")

# Operation choice and calculation
if st.session_state.initialized and 'state' in st.session_state and st.session_state.state == 'operation':
    operation = st.radio("What do you want to do?", ('add', 'subtract'), key="operation_select")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        num1 = st.number_input("Enter first number:", format="%d", key="num1")
    with col2:
        num2 = st.number_input("Enter second number:", format="%d", key="num2")
    with col3:
        if st.button("Calculate", key="calculate"):
            user_answer = st.number_input("What is the result?", format="%d", key="user_ans")
            response = handle_response(num1, num2, user_answer, operation)
            st.write(response)

