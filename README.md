🧠 RanchoBot – An AI-Powered Chatbot Inspired by 3 Idiots
RanchoBot is a personality-rich chatbot inspired by the legendary character Ranchoddas Shamaldas Chanchad (Rancho) from the movie 3 Idiots. Built using Python and Tkinter, this chatbot delivers quirky, motivational, and witty responses — now powered by Cohere AI for smarter, more dynamic interactions.

| Feature                             | Description                                                      |
| ----------------------------------- | ---------------------------------------------------------------- |
| 🤖 **AI-Powered Replies**           | Uses Cohere’s command models to generate Rancho-style responses. |
| 🖥️ **Graphical Chat Interface**    | Built with Tkinter, including a terminal-style dark theme.       |
| 🧠 **Rancho Personality**           | Replies reflect Rancho’s wisdom, humor, and desi-friendliness.   |
| 💾 **Chat Log Saving**              | Automatically saves chat history to a file (optional).           |

.
🧪 How It Works
User types a message into the input box.

The message is sent to the Cohere API for processing.

Based on context and character prompt, a Rancho-style reply is generated.

The reply is displayed in the GUI, optionally spoken using text-to-speech.

| Technology             | Purpose                     |
| ---------------------- | --------------------------- |
| Python 3.10+           | Core development            |
| Tkinter                | GUI framework               |
| Cohere API             | Smart AI responses          |
| `cohere` Python SDK    | Connects to Cohere’s models |
| `pyttsx3` *(optional)* | Text-to-speech              |
| `Pillow` *(optional)*  | Avatar/image handling       |

📦 Folder Structure
Rancho Chatot/
│
├── rancho_gui.py         # Main GUI application
├── chatbot_logic.py      # AI interaction with Cohere API
├── assets/
│   ├── rancho.png        # Optional: Avatar image
│   └── sounds/           # Optional: Sound effects
├── README.md             # Project overview
├── requirements.txt      # Python dependencies
└── .env                  # Securely stores API key

