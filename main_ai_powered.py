//here is the upgraded which is powered by AI
import tkinter as tk
from tkinter import scrolledtext
import cohere

# ------------------- Cohere API Setup ------------------- #
COHERE_API_KEY = "NS30PuoSDzQZQaVqk37t861xaNKfxeTzUKfzu8Re"
co = cohere.Client(COHERE_API_KEY)

# ------------------- Rancho AI Logic ------------------- #
def ask_rancho(user_input):
    try:
        response = co.chat(
            model="command-r-plus",
            message=user_input,
            chat_history=[],
            temperature=0.8,
            prompt_truncation='auto',
            connectors=[],
            preamble=(
                "You are Rancho (Ranchoddas Shamaldas Chanchad), the brilliant, witty, and inspiring character from the Bollywood movie '3 Idiots'. "
                "You are a fun-loving, deeply philosophical Indian engineering student. Your replies are filled with wisdom, humor, and desi-style motivation. "
                "You often use phrases like 'All is well', 'Excellence ke peeche bhaago', and encourage learning by heart, not by rote. "
                "Talk in a friendly, casual, Indian tone. Be clever, insightful, and slightly cheeky when needed."
            )
        )
        return response.text.strip()
    except Exception as e:
        return "Arre yaar, Rancho ki signal weak hai... Try again later!"

# ------------------- GUI Setup ------------------- #
def send_message():
    user_message = user_input.get()
    if user_message.strip() == "":
        return

    chat_area.insert(tk.END, "You: " + user_message + "\n", "user")
    response = ask_rancho(user_message)
    chat_area.insert(tk.END, "Rancho: " + response + "\n\n", "bot")
    user_input.delete(0, tk.END)

# ------------------- Main Window ------------------- #
window = tk.Tk()
window.title("RanchoBot – AI Chat with Rancho 🤖")
window.geometry("540x550")
window.config(bg="black")

# Title
title_label = tk.Label(window, text="🧠 Chat with Rancho", font=("Arial", 18, "bold"), bg="black", fg="lightgreen")
title_label.pack(pady=10)

# Chat display area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20, font=("Courier", 11), bg="black", fg="white", insertbackground="white")
chat_area.pack(padx=10, pady=10)
chat_area.tag_config("user", foreground="cyan")
chat_area.tag_config("bot", foreground="lightgreen")

# Entry field
user_input = tk.Entry(window, font=("Arial", 12), bg="#222", fg="white", insertbackground="white")
user_input.pack(padx=10, pady=5, fill=tk.X)

# Send button
send_button = tk.Button(window, text="Send", command=send_message, font=("Arial", 12), bg="#444", fg="white")
send_button.pack(pady=5)

# Start GUI
window.mainloop()
