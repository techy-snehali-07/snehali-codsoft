🧠 RanchoBot – A GUI-Based Rule-Based Chatbot Inspired by 3 Idiots
Welcome to RanchoBot — a rule-based chatbot built to simulate the iconic character Ranchoddas Shamaldas Chanchad (Rancho) from the movie 3 Idiots. Designed with humor, wisdom, and inspiration in mind, this bot provides personality-rich responses based on classic Rancho philosophies.
🎯 Features
🧠 Rule-Based Intelligence
Provides predefined responses using if-else logic based on keywords.
🖥️ Graphical Chat Interface
Built using Tkinter, offering a clean and interactive user interface.

🎨 Dark Theme GUI
Terminal-style dark mode interface for a modern, coder-friendly feel.

📜 Character Consistency
Mimics Rancho's style — motivational, witty, and knowledge-driven.

💬 Real-Time Chat Simulation
Supports continuous interaction with live message feed.
| Technology                           | Purpose                     |
| ------------------------------------ | --------------------------- |
| **Python 3.10+**                     | Core programming language   |
| **Tkinter**                          | GUI development             |
| **ScrolledText**                     | Scrollable chat area        |
| **Custom Logic**                     | Rule-based keyword matching |
| `Cohere/OpenAI API` *(future scope)* | For smarter AI replies      |

🧪 How It Works
User types a message in the input box.

The chatbot scans for key phrases like "exam", "machine", "all is well", etc.

Based on matches, it gives motivational or witty replies that reflect Rancho's style.

Responses are printed to the chat area with user-bot format.

The interface has a black background with light-colored text for readability and theme.

📦 Folder Structure Suggestion
RanchoBot/
│
├── rancho_gui.py            # Main GUI Application
├── chatbot_logic.py         # Contains ask_rancho() function
├── assets/                  # Optional: for sound, icons
├── README.md                # Project Description
└── requirements.txt         # List of dependencies (e.g., Tkinter, pyttsx3)
