import datetime
import json
import os

LOG_FILE = "chat_log.json"

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []

def save_log(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

def get_intent(message):
    msg = message.lower()
    if any(x in msg for x in ["hello", "hi", "hey"]):
        return "greeting"
    if "time" in msg:
        return "time"
    if "date" in msg:
        return "date"
    if "your name" in msg:
        return "name"
    if "bye" in msg:
        return "exit"
    return "unknown"

def respond(intent, context):
    if intent == "greeting":
        return "Hello! How can I help you today?"
    if intent == "time":
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
    if intent == "date":
        return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}."
    if intent == "name":
        return "I am a smart offline chatbot built in Python."
    if intent == "exit":
        return "Goodbye! Have a great day."
    return "I'm not sure how to respond to that yet."

def main():
    print("🧠 Smart CLI Chatbot ")
    print("Type 'bye' to exit.\n")

    chat_log = load_log()
    context = {}

    while True:
        user = input("You: ")
        intent = get_intent(user)
        reply = respond(intent, context)

        chat_log.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "user": user,
            "bot": reply
        })
        save_log(chat_log)

        print("Bot:", reply)

        if intent == "exit":
            break

if __name__ == "__main__":
    main()
