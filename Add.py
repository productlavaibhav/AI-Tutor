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
    st.session_state['example_index'] = 0

def get_example(num1, num2, operation):
    # Selecting subject based on the random index
    subjects = ["toy cars", "stickers", "books", "pencils", "apples", "coins"]
    subject = subjects[st.session_state.example_index % len(subjects)]
    st.session_state.example_index += 1

    if operation == 'add':
        return f"Imagine you have {num1} {subject} and gain {num2} more. How many {subject} do you have now?"
    elif operation == 'subtract':
        if num1 >= num2:
            return f"You have {num1} {subject}. You need to give away {num2} {subject}. Start removing them one by one."
        else:
            needed = num2 - num1
            return (f"You have {num1} {subject} (imagine {num1} {subject}). "
                    f"You need to give away {num2} {subject}. After giving away all {num1}, "
                    f"you still need to give {needed} more. Now, you owe {needed} {subject}.")

def handle_response(num1, num2, user_answer, operation):
    operations = {
        "add": num1 + num2,
        "subtract": num1 - num2
    }
    correct_answer = operations[operation]
    difference = abs(user_answer - correct_answer)
    response = ""
    
    if user_answer == correct_answer:
        response = "That's correct! 🎉 Great job! Try another one?"
        st.session_state.attempts = 0
    else:
        if st.session_state.attempts > 0:
            if difference < st.session_state.previous_difference:
                response = "You're getting closer! 😊 Keep trying, you're doing well!"
            elif difference == st.session_state.previous_difference:
                response = "You're close, but just as close as last time. Try tweaking your answer a bit!"
            else:
                response = "It seems like you're moving away from the correct answer. 😟 Let's try another way."
        else:
            response = "That’s not quite right. 😕 Here’s an example to help you think about it:"
        
        example = get_example(num1, num2, operation)
        response += f" {example}"
        st.session_state.attempts += 1
        st.session_state.previous_difference = difference

    return response

# Navigation function
def go_back():
    if st.session_state['initialized']:
        st.session_state['initialized'] = False

# Navigation Button
if st.session_state['initialized']:
    st.button("Go Back", on_click=go_back)

# Step 1: Ask for the user's name
if not st.session_state['initialized']:
    name = st.text_input("What's your name?", key="name_input")
    if name:
        st.session_state['name'] = name
        st.session_state['initialized'] = True

# Step 2: Ask what operation they want to perform
if st.session_state['initialized'] and not st.session_state['operation']:
    operation = st.radio("What would you like to do today?", ('add', 'subtract'), key="operation_select")
    st.session_state['operation'] = operation

# Step 3: Show the fields for input numbers and response
if st.session_state['operation']:
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number:", format="%d", key="num1")
    with col2:
        num2 = st.number_input("Enter second number:", format="%d", key="num2")
    
    user_answer = st.number_input("What is the result?", format="%d", key="user_ans")
    submit = st.button("Check my answer", key="submit")

    # Step 4: Handle the response based on user's answer
    if submit:
        response = handle_response(num1, num2, user_answer, st.session_state['operation'])
        st.write(response)
