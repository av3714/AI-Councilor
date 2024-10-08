import streamlit as st
import google.generativeai as palm

# Configure the generative AI model and API key
palm.configure(api_key='AIzaSyBZZBj_c1TDDWAYgDg8GUqGiJYX4uzSjxY')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

st.title("Student Career Counselor Chatbot")

# Initial chatbot response
chatbot = palm.chat(context="Act like a Student Career Counsellor.")  # Initialize the chatbot

# Display the initial message
st.write("Hello, I'm your Student Career Counselor, how can I help you?")

# Input for user message
user_message = st.text_input("Enter your message:")

if user_message:
    # Send the user's message to the chatbot
    chatbot.reply(user_message)
    
    # Get the bot's response
    response = chatbot.response
    st.write("Bot:", response.last)  # Display the bot's response
