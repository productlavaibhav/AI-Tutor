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

def get_example(num1, num2, operation):
    subjects = ["toy cars", "stickers", "books", "pencils", "apples", "coins"]
    subject = subjects[random.randint(0, len(subjects) - 1)]

    if operation == 'add':
        return f"Imagine you have {num1} {subject} and gain {num2} more. How many {subject} do you have now?"
    else:  # For 'subtract'
        return f"If you had {num1} {subject} and lost {num2}, how many {subject} would you have left?"

def handle_response(num1, num2, user_answer, operation):
    num1 = int(num1)  # Ensure num1 is an integer
    num2 = int(num2)  # Ensure num2 is an integer
    user_answer = int(user_answer)  # Ensure user_answer is an integer

    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y
    }
    correct_answer = operations[operation](num1, num2)
    difference = abs(user_answer - correct_answer)
    response = ""

    if user_answer == correct_answer:
        response = "That's correct! 🎉 Great job!"
    else:
        response = "That’s not quite right. 😕"
        example = get_example(num1, num2, operation)
        response += f" Here’s an example to help you think about it: {example}"

    return response

# Step 1: Ask for the user's name
if 'name' not in st.session_state or not st.session_state.name:
    name = st.text_input("What's your name?", key="name_input")
    if name:
        st.session_state.name = name
        st.session_state.initialized = True

# Step 2: Ask what operation they want to perform
if st.session_state.initialized and not st.session_state.operation:
    operation = st.radio("What would you like to do today?", ('add', 'subtract'), key="operation_select")
    if operation:
        st.session_state.operation = operation

# Step 3: Show the fields for input numbers and response
if st.session_state.operation:
    num1 = st.number_input("Enter first number:", format="%d", key="num1")
    num2 = st.number_input("Enter second number:", format="%d", key="num2")
    user_answer = st.number_input("What is the result?", format="%d", key="user_ans")
    submit = st.button("Check my answer", key="submit")

    # Step 4: Handle the response based on user's answer
    if submit:
        response = handle_response(num1, num2, user_answer, st.session_state.operation)
        st.write(response)
