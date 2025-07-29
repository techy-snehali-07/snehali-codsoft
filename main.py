import tkinter as tk
from tkinter import scrolledtext

# ------------------- Rancho Chatbot Logic ------------------- #
def ask_rancho(user_input):
    user_input = user_input.lower()

    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return "Arre yaar, hello! All is well? 😊"
    elif "exam" in user_input or "marks" in user_input:
        return "Bhai, don’t chase marks. Chase excellence. Success will follow."
    elif "pressure" in user_input or "stress" in user_input:
        return "Life is not a race. Relax. Take a deep breath. ALL IS WELL. 🙂"
    elif "machine" in user_input:
        return "A machine is anything that reduces human effort. Simple, na?"
    elif "virus" in user_input:
        return "Virus is not just a person... he’s a whole mood. 😅"
    elif "quote" in user_input:
        return "Famous Rancho quote: 'Pursue excellence, and success will follow.'"
    elif "all is well" in user_input:
        return "ALL IS WELL! Say it from the heart. It may not fix problems, but it gives strength."
    elif "love" in user_input:
        return "Love? Arre, that’s not in the syllabus... but it's important too."
    elif "career" in user_input:
        return "Follow your passion. Engineer ho ya photographer — be excellent."
    elif "bye" in user_input:
        return "Chal, milte hain. Remember: All is well."
    else:
        return "Hmm... interesting. But remember, seek knowledge, not marks."


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
window.geometry("500x500")
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
