# Step 1: Install Required Libraries
pip install requests

# Step 2: Import Libraries
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

# Step 6: Run the Chatbot in an Interactive Loop
print("Chatbot: Hi! I'm here to help. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ").lower()
    
    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    
    response = get_response(user_input)
    print(f"Chatbot: {response}")
