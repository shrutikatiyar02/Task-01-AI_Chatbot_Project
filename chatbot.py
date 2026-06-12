# ==========================================
# AI RULE-BASED CHATBOT PROJECT
# Name: Shruti Katiyar
# ==========================================

import datetime
import random

# -----------------------------
# Motivational Quotes
# -----------------------------
quotes = [
    "Believe in yourself!",
    "Success comes from hard work.",
    "Never give up!",
    "You are capable of amazing things.",
    "Keep learning and growing."
]


# -----------------------------
# Function to Save Chat
# -----------------------------
def save_chat(message):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")


# -----------------------------
# Welcome Screen
# -----------------------------
print("=" * 50)
print("WELCOME TO AI CHATBOT")
print("=" * 50)

name = input("Enter your name: ").strip().title()

print(f"\nHello {name}! 😊")
print("I am your chatbot assistant.")

print("Type 'help' to see commands.")
print("Type 'bye' anytime to exit.\n")

save_chat("\n===== New Chat Started =====")


# -----------------------------
# Chatbot Loop
# -----------------------------
while True:

    user = input("You: ").lower().strip()

    save_chat(f"{name}: {user}")

    # Greetings
    if user in ["hi", "hello", "hey"]:
        response = f"Hello {name}! How can I help you today? 😊"

    # Name
    elif "your name" in user:
        response = "I'm an AI Chatbot created to help you."

    # How are you
    elif "how are you" in user:
        response = "I'm doing great! Thanks for asking."

    # Good Morning
    elif "good morning" in user:
        response = "Good Morning! Hope you have a great day ☀️"

    # Good Evening
    elif "good evening" in user:
        response = "Good Evening! Hope your day went well 🌙"

    # Time
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}"

    # Date
    elif "date" in user:
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        response = f"Today's date is {today}"

    # AI Meaning
    elif "what is ai" in user:
        response = (
            "AI means Artificial Intelligence. "
            "It helps machines learn, think, and solve problems."
        )

    # Motivation
    elif "motivate me" in user:
        response = random.choice(quotes)

    # Thank You
    elif "thank you" in user or "thanks" in user:
        response = "You're welcome! Happy to help 😊"

    # Help Menu
    elif user == "help":
        response = """
Available Commands:
• hi / hello
• how are you
• your name
• time
• date
• what is ai
• motivate me
• good morning
• good evening
• thank you
• bye
"""

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day 😊")
        save_chat("Bot: Goodbye! Have a nice day 😊")
        break

    # Unknown Input
    else:
        response = "Sorry, I didn't understand that. Try typing 'help'."

    # Show Response
    print("Bot:", response)

    # Save Bot Reply
    save_chat(f"Bot: {response}")