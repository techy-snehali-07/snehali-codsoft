//here is the upgraded which is powered by AI

import tkinter as tk
from tkinter import scrolledtext
import cohere
import os

# ------------------- Cohere API Setup ------------------- #
COHERE_API_KEY = "NS30PuoSDzQZQaVqk37t861xaNKfxeTzUKfzu8Re" 
co = cohere.Client(COHERE_API_KEY)

# ------------------- Rancho AI Logic ------------------- #
def ask_rancho(user_input):
    try:
        response = co.chat(
            model="command-r-plus",  # Use "command-r" if "plus" is unavailable
            message=user_input,
            chat_history=[],
            temperature=0.7,
            prompt_truncation='auto',
            connectors=[],
            preamble="You are Rancho from the movie 3 Idiots. You speak like a witty, inspiring engineering student. Your replies are friendly, philosophical, and Indian-style quirky."
        )
        return response.text
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

# Create main window
window = tk.Tk()
window.title("Rancho Chatbot 🤖")
window.geometry("520x500")
window.config(bg="black")

# Title Label
title_label = tk.Label(window, text="Chat with Rancho 🧠", font=("Arial", 16, "bold"), bg="black", fg="lightgreen")
title_label.pack(pady=10)

# Chat display area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20, font=("Courier", 11), bg="black", fg="white", insertbackground="white")
chat_area.pack(padx=10, pady=5)
chat_area.config(state=tk.NORMAL)

# Text tag styles
chat_area.tag_config("user", foreground="cyan")
chat_area.tag_config("bot", foreground="lightgreen")

# Entry box
user_input = tk.Entry(window, font=("Arial", 12), bg="#222", fg="white", insertbackground="white")
user_input.pack(padx=10, pady=10, fill=tk.X)

# Send button
send_button = tk.Button(window, text="Send", command=send_message, font=("Arial", 12), bg="#444", fg="white")
send_button.pack(pady=5)

# Run app
window.mainloop()
