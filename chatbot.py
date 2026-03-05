import tkinter as tk
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ai(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.1:8b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def send_message():

    user_msg = entry.get()

    if user_msg == "":
        return

    chat.insert(tk.END, "You: " + user_msg + "\n")

    bot_reply = ask_ai(user_msg)

    chat.insert(tk.END, "Bot: " + bot_reply + "\n\n")

    entry.delete(0, tk.END)


window = tk.Tk()
window.title("AI Chatbot - Ujjwal Prakash")
window.geometry("500x500")

chat = tk.Text(window)
chat.pack(pady=10)

entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT, padx=10)

send = tk.Button(window, text="Send", command=send_message)
send.pack(side=tk.LEFT)

window.mainloop()