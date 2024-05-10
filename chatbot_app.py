import streamlit as st
import requests

# Function to send a message to Rasa and get the response
def get_bot_response(user_message):
    rasa_endpoint = "http://localhost:5055/webhook"  # Update with your Rasa endpoint
    payload = {"message": user_message}
    response = requests.post(rasa_endpoint, json=payload)
    return response.json()

# Set Streamlit page configuration as the first command
st.set_page_config(layout="wide")

# Streamlit layout
st.title("Rasa Chatbot")

# User input text box
user_input = st.text_input("You:", "")

# Chat history area
chat_history = st.empty()

if st.button("Send"):
    user_message = user_input.strip()
    if user_message:
        # Display user message
        chat_history.text(f"You: {user_message}")

        # Get bot response
        bot_response = get_bot_response(user_message)

        # Display bot response
        for response in bot_response:
            chat_history.text(f"Bot: {response['text']}")
