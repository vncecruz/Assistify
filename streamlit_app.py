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

# Function to greet the user
def greet_user(name):
    return f"Hello, {name}! How can I assist you today?"

# Function to generate a response based on sentiment intensity
def generate_response(user_input, user_name):
    sentiment = detect_sentiment_intensity(user_input)
    response_options = responses.get(sentiment, [f"I'm here to help, {user_name}!"])
    return random.choice(response_options)

# Ask for user's name
user_name = input("Please enter your name: ")
print("Chatbot:", greet_user(user_name))

# Conversation history list to track all interactions
conversation_history = []

# Chat loop for custom user input with exit option
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'stop']:
        print("Chatbot: Goodbye!")
        break

    # Generate and display chatbot response
    response = generate_response(user_input, user_name)
    print("Chatbot:", response)
    print("-" * 30)

    # Append to conversation history
    conversation_history.append({"user": user_input, "bot": response})

# Print full conversation history at the end
for turn in conversation_history:
    print("User:", turn["user"])
    print("Chatbot:", turn["bot"])
    print("-" * 30)
