import streamlit as st
from textblob import TextBlob
import random

# Function to detect sentiment with intensity
def detect_sentiment_intensity(message):
    analysis = TextBlob(message)
    polarity = analysis.sentiment.polarity
    if polarity > 0.5:
        return "strongly positive"
    elif polarity > 0:
        return "mildly positive"
    elif polarity < -0.5:
        return "strongly negative"
    elif polarity < 0:
        return "mildly negative"
    else:
        return "neutral"

# Define responses with emojis for each sentiment intensity
responses = {
    "strongly positive": ["That's fantastic! 😊 We’re thrilled you’re happy with our service."],
    "mildly positive": ["Thanks for your feedback! 😊 Glad to know you’re satisfied."],
    "neutral": ["Thanks for reaching out. 😊 Let us know if you have any questions!"],
    "mildly negative": ["We apologize if things didn’t meet your expectations. 😟 How can we help?"],
    "strongly negative": ["We’re really sorry to hear that. 😞 Please contact support, and we’ll assist you immediately."],
}

# Streamlit app setup
st.title("Assistify 🛒")
st.sidebar.header("Chatbot Settings")

# Function to greet the user
def greet_user(name):
    return f"Hello, {name}! How can I assist you today?"

# Function to generate a response based on sentiment intensity
def generate_response(user_input, user_name):
    sentiment = detect_sentiment_intensity(user_input)
    response_options = responses.get(sentiment, [f"I'm here to help, {user_name}!"])
    return random.choice(response_options)

# Initialize conversation history in Streamlit session state
if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []

# User name input
user_name = st.sidebar.text_input("Enter your name", "Guest")

# Greet user if name provided
if user_name:
    st.write(greet_user(user_name))

# User message input
user_input = st.text_input("You:", "")

# Generate response on button click
if st.button("Send"):
    if user_input.strip():
        response = generate_response(user_input, user_name)
        # Save the interaction in conversation history
        st.session_state["conversation_history"].append({"user": user_input, "bot": response})
    else:
        st.warning("Please enter a message.")

# Display conversation history with indentation
for turn in st.session_state["conversation_history"]:
    st.markdown(f"**You:** {turn['user']}")
    st.markdown(f"<div style='margin-left: 20px;'>Assistify: {turn['bot']}</div>", unsafe_allow_html=True)
