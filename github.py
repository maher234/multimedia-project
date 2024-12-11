import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            tts = gTTS(text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == "nt" else "open output.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter your text ")

def delet_text():
    text_entry.delete("1.0", tk.END)

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Text To Speech ")
root.geometry("600x500")

tk.Label(root,text="Text To Speech",bg="red", font=("Arial",20 )).pack(pady=10)
tk.Label(root,text="Enter your text ",font=("Arial",25),bg="yellow").pack(pady=30)
# Create a text entry widget
text_entry = tk.Text(root, wrap=tk.WORD, height=3, width=40)
text_entry.pack(pady=10)

# Create buttons
play_button = tk.Button(root, text="Play",bg="blue", command=play_text)
play_button.pack(pady=10)

set_button = tk.Button(root, text="set", bg="green",command=delet_text)
set_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit",bg="red", command=exit_app)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
