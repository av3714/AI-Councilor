import streamlit as st
import google.generativeai as palm

# Configure the generative AI model and API key
palm.configure(api_key='AIzaSyBZZBj_c1TDDWAYgDg8GUqGiJYX4uzSjxY')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

st.title("Student Career Counselor Chatbot")

# Initial chatbot response context
chat_context = "Act like a Student Career Counsellor."

# Display the initial message
st.write("Hello, I'm your Student Career Counselor, how can I help you?")

# Input for user message
user_message = st.text_input("Enter your message:")

if user_message:
    try:
        # Send the user's message to the chatbot
        response = palm.generate_text(
            model=model,
            prompt=f"{chat_context}\nUser: {user_message}\nBot:",
            temperature=0.7,
            max_output_tokens=200,
        )
        # Display the bot's response
        if response.result:
            st.write("Bot:", response.result)
        else:
            st.write("Bot: Sorry, I couldn't generate a response. Please try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
