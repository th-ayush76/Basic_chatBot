# Author: Ayush
# Project: Basic Rule-Based Chatbot
# Description: A simple chatbot that replies to predefined user inputs

def get_response(user_input):
    """Return a reply based on the user's input."""
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hello", "hi", "hey", "hii"]:
        return "Hi there! 👋 How can I help you?"

    # How are you
    elif user_input in ["how are you", "how are you?", "how r you", "how do you do"]:
        return "I'm doing great, thanks for asking! 😊 How about you?"

    # User is fine
    elif user_input in ["i'm fine", "i am fine", "good", "fine", "great", "i'm good"]:
        return "That's wonderful to hear! 🌟"

    # Name
    elif user_input in ["what is your name", "what's your name", "your name"]:
        return "I'm AyushBot 🤖 — your simple rule-based assistant!"

    # Age
    elif user_input in ["how old are you", "your age", "what is your age"]:
        return "I was just created, so I'm brand new! 😄"

    # What can you do
    elif user_input in ["what can you do", "help", "what do you do"]:
        return "I can chat with you! Try saying: hello, how are you, tell me a joke, or bye."

    # Joke
    elif user_input in ["tell me a joke", "joke", "say something funny"]:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 😂"

    # Favorite language
    elif user_input in ["favorite language", "favourite language", "best language"]:
        return "Python, of course! 🐍 Simple, powerful, and elegant."

    # Time
    elif user_input in ["what time is it", "time", "current time"]:
        import datetime
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now} ⏰"

    # Date
    elif user_input in ["what is today's date", "today's date", "date", "what date is it"]:
        import datetime
        today = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today is {today} 📅"

    # Thanks
    elif user_input in ["thanks", "thank you", "thankyou", "thx"]:
        return "You're welcome! 😊 Always happy to help."

    # Goodbye
    elif user_input in ["bye", "goodbye", "see you", "exit", "quit", "see ya"]:
        return "Goodbye! 👋 Have a wonderful day!"

    # Unknown input
    else:
        return "Hmm, I didn't quite get that. 🤔 Try: hello, how are you, joke, or bye."


# ─────────────────────────────────────────
#  Main chat loop
# ─────────────────────────────────────────

def main():
    print("=" * 45)
    print("        Welcome to AyushBot 🤖")
    print("     A Simple Rule-Based Chatbot")
    print("       Made by Ayush")
    print("=" * 45)
    print("  Type 'bye' to exit the chat.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something! 😊\n")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}\n")

        # Exit condition
        if user_input.lower() in ["bye", "goodbye", "see you", "exit", "quit", "see ya"]:
            break


# ─────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────

if __name__ == "__main__":
    main()