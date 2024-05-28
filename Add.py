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
        examples = [
            f"Imagine you have {num1} apples and find {num2} more. How many apples do you have in total?",
            f"You have {num1} crayons, and your friend gives you {num2} more. How many crayons do you have now?",
            f"There are {num1} birds on a tree, and {num2} more birds come to join them. How many birds are there now?"
        ]
    else:
        action = "subtracting"
        if num1 >= num2:
            examples = [
                f"You have {num1} cookies, and you eat {num2} of them. How many cookies are left?",
                f"You have {num1} balloons, and {num2} pop. How many balloons are left?",
                f"You have {num1} candies, and you give {num2} to your friend. How many candies do you have left?"
            ]
        else:
            examples = [
                f"You have {num1} toy cars. You need to give away {num2} toy cars.  Since you only have {num1}, you'll have to give away all of them and still owe some!  How many will you owe?",
                f"You have {num1} marbles, and you want to give {num2} to your friends. You don't have enough!  How many more marbles would you need to give away all {num2}?",
                f"You have {num1} stickers. You want to give {num2} to your classmates. You don't have enough! How many more stickers would you need to give away all {num2}?"
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

# **Define the function outside the conditional block**
def get_emotional_reply(response):
    positive_keywords = ["good", "great", "well", "amazing"]
    negative_keywords = ["bad", "not good", "terrible", "sad"]

    for keyword in positive_keywords:
        if keyword in response.lower():
            return "That's awesome! 😊 Let's dive into some math problems!"
    for keyword in negative_keywords:
        if keyword in response.lower():
            return "Oh, I'm sorry to hear that. 😔  Maybe some math can help you feel better! Let's try it!"
    return "Okay, let's get started! 🚀"


# Step 1: Ask for the user's name
if 'name' not in st.session_state or not st.session_state['name']:
    st.session_state['name'] = st.text_input("What's your name?", key="name_input")

# Step 2: Ask how they are doing
if st.session_state['name'] and not st.session_state.initialized:
    response = st.text_input(f"Hello, {st.session_state['name']}! How are you doing today?", key="emotion_input")
    if response:
        st.session_state.initialized = True
        emotional_reply = get_emotional_reply(response)
        st.write(emotional_reply)

# Step 4: Ask what operation they want to perform
if st.session_state.initialized:
    operation = st.radio("What do you want to do?", ('add', 'subtract'), key="operation_select")

    # Step 5: Show the fields for input numbers and response
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number:", format="%d", key="num1", step=1) # Add step=1 to control input as integer only
    with col2:
        num2 = st.number_input("Enter second number:", format="%d", key="num2", step=1) # Add step=1 to control input as integer only
    
    user_answer = st.number_input("What is the result?", format="%d", key="user_ans", step=1) # Add step=1 to control input as integer only
    submit = st.button("Check my answer", key="submit")

    # Step 6: Handle the response based on user's answer
    if submit and operation:
        response = handle_response(num1, num2, user_answer, operation)
        st.write(response)

    # Add a back button
    if st.button("Back to Main Menu"):
        st.session_state.initialized = False
        st.session_state.name = ""
        st.session_state.operation = None
        st.session_state.attempts = 0
        st.session_state.previous_difference = float('inf')
