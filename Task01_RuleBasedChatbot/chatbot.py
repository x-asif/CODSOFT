# Task01_RuleBasedChatbot/chatbot.py
import tkinter as tk

# -------------------------------
# Rule-based chatbot function
# -------------------------------
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"
    elif "name" in user_input:
        return "I am Asif's Rule-Based Chatbot 🤖."
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"
    elif "weather" in user_input:
        return "I can't check live weather, but it's always a good time to code! 🌞"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    elif "help" in user_input:
        return "I can answer greetings, my name, weather, jokes and more!"
    elif "joke" in user_input:
        return "Why did the computer go to the doctor? Because it caught a virus! 😂"
    else:
        return "Sorry, I don't understand that. Could you rephrase?"

# -------------------------------
# GUI Functions
# -------------------------------
def send_message():
    user_input = entry.get()
    if user_input.strip() != "":
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        response = chatbot_response(user_input)
        chat_window.insert(tk.END, "Bot: " + response + "\n\n")
        chat_window.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Asif's Rule-Based Chatbot 🤖")
root.geometry("500x500")

chat_window = tk.Text(root, bd=1, bg="lightyellow", width=60, height=25, wrap="word")
chat_window.config(state=tk.DISABLED)
chat_window.pack(padx=10, pady=10)

entry = tk.Entry(root, bd=1, width=40, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

root.mainloop()
