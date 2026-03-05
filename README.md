# 🤖 AI GUI Chatbot (Tkinter + Ollama)

A simple **AI-powered desktop chatbot** built using **Python Tkinter GUI** and **Ollama local LLM**.
The chatbot provides a graphical interface where users can chat with a local AI model directly from their desktop.

---

## ✨ Features

* 💬 Chat with a local AI model
* 🖥 Simple desktop GUI built with Tkinter
* ⚡ Fast responses using Ollama API
* 🔒 Fully local AI (no internet required after model download)
* 🧠 Uses powerful open-source LLMs like `llama3.1:8b`

---

## 📸 Preview

Example interaction:

```
You: Hello
Bot: Hello! How can I help you today?
```

---

## 🛠 Technologies Used

* Python
* Tkinter (GUI framework)
* Ollama (local LLM runtime)
* Requests (API communication)

---

## 📂 Project Structure

```
ai-gui-chatbot
│
├── chatbot.py        # Main chatbot application
├── README.md         # Project documentation
└── requirements.txt  # Python dependencies
```

---

## 🚀 Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/ai-gui-chatbot.git
cd ai-gui-chatbot
```

---

### 2️⃣ Install Python dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Install Ollama

Download and install from:

https://ollama.com

---

### 4️⃣ Download AI model

Example:

```
ollama pull llama3.1:8b
```

---

### 5️⃣ Run the chatbot

```
python chatbot.py
```

A GUI window will open where you can chat with the AI.

---

## ⚙️ Configuration

If you want to change the model, edit the model name inside `chatbot.py`.

Example:

```python
"model": "llama3.1:8b"
```

You can also use other models supported by Ollama.

---

## 💡 Future Improvements

* Chat history memory
* Streaming AI responses
* Dark theme UI
* Voice input support
* Chat bubbles like ChatGPT

---

## 👨‍💻 Author

**Ujjwal Prakash (Dhoni)**

---

## ⭐ Support

If you like this project, consider **starring the repository on GitHub**.
