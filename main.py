# Step 1: Install Required Libraries
# Run this command in your terminal to install Streamlit:
# pip install streamlit requests

# Step 2: Import Libraries
import streamlit as st
import requests
import json

# Step 3: Define Your Gemini API Key
GEMINI_API_KEY = "AIzaSyDnOIewAcFdrq-lLQP4LzJePJTLkAZ4UMY"  # Replace with your actual Gemini API key

# Step 4: Define the Gemini API Endpoint
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# Step 5: Define the Chatbot Function
def get_response(user_input):
    try:
        # Prepare the request payload
        payload = {
            "contents": [{
                "parts": [{"text": user_input}]
            }]
        }
        
        # Make the POST request to the Gemini API
        headers = {
            "Content-Type": "application/json"
        }
        params = {
            "key": GEMINI_API_KEY
        }
        response = requests.post(API_URL, headers=headers, params=params, data=json.dumps(payload))
        
        # Parse the response
        if response.status_code == 200:
            response_data = response.json()
            # Extract the generated text from the response
            generated_text = response_data['candidates'][0]['content']['parts'][0]['text']
            return generated_text.strip()
        else:
            return f"Error: {response.status_code}, {response.text}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Step 6: Create the Streamlit UI
def main():
    # Set the title of the app
    st.title("💬 Chatbot Powered by Gemini API")
    st.write("Hi! I'm here to help. Type your message below and I'll respond!")

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get user input
    user_input = st.chat_input("Type your message here...")

    if user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Get chatbot response
        bot_response = get_response(user_input)

        # Add bot response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": bot_response})

        # Display bot response
        with st.chat_message("assistant"):
            st.markdown(bot_response)

# Step 7: Run the App
if __name__ == "__main__":
    main()
