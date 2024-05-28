import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Interactive Math Tutor")

st.header("Interactive Math Tutor")

# Initialize session variables if they don't exist
if 'initialized' not in st.session_state:
    st.session_state.initialized = False
    st.session_state.name = ""
    st.session_state.operation = None

def get_example(num1, num2, operation):
    if operation == 'add':
        action = "gain"
        scenario = "How many do you have now?"
    else:
        action = "lose"
        scenario = "How many do you have left?"
    
    examples = [
        f"Imagine you have {num1} candies and you {action} {num2}. {scenario}",
        f"If you had {num1} apples and you {action} {num2} apples, {scenario}"
    ]

    return random.choice(examples)

def handle_response(num1, num2, user_answer, operation):
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
        if difference < 5:
            response = "You're very close! 😊 Keep trying!"
        elif difference < 10:
            response = "Not quite right, but you're on the right track. 🤔"
        else:
            response = "It seems you're a bit far from the correct answer. 😟 Let's try another example."
        
        example = get_example(num1, num2, operation)
        response += f" {example}"

    return response

# Step 1: Ask for the user's name if it has not been set
if 'name' not in st.session_state or not st.session_state.name:
    st.session_state.name = st.text_input("What's your name?", key="name_input")
    if st.session_state.name:
        st.session_state.initialized = True

# Step 2: Ask what operation they want to perform
if st.session_state.initialized and not st.session_state.operation:
    st.session_state.operation = st.radio("What would you like to do today?", ('add', 'subtract'), key="operation_select")

# Step 3: Show the fields for input numbers and response
if st.session_state.operation:
    num1 = st.number_input("Enter first number:", format="%d", key="num1")
    num2 = st.number_input("Enter second number:", format="%d", key="num2")
    user_answer = st.number_input("What is the result?", format="%d", key="user_ans")
    if st.button("Check my answer", key="submit"):
        response = handle_response(num1, num2, user_answer, st.session_state.operation)
        st.write(response)
