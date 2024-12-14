import os
from gtts import gTTS
import tkinter as tk
from tkinter import messagebox
from playsound import playsound 

# Function to convert text to speech and play it
def play_text():
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Warning", "No text entered!")
        return
    try:
        # Convert text to speech and save as audio file
        tts = gTTS(text)
        audio_file = "output.mp3"
        tts.save(audio_file)

        # Play the audio file
        playsound(audio_file)

        # Optionally delete the file after playing
        os.remove(audio_file)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to clear the text
def clear_text():
    entry.delete(0, tk.END)  # Clears the text in the entry widget

# Function to exit the application
def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Text to Speech")

# Set the window size
root.geometry("300x200")

# Add title label
title_label = tk.Label(root, text="Text to Speech", font=("Arial", 14))
title_label.pack(pady=10)

# Add entry label
entry_label = tk.Label(root, text="Enter your text:")
entry_label.pack()

# Add text entry box
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Add buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

play_button = tk.Button(button_frame, text="Play", command=play_text)
play_button.grid(row=0, column=0, padx=5)

exit_button = tk.Button(button_frame, text="Exit",bg="red", command=exit_app)
exit_button.grid(row=0, column=1, padx=5)

set_button = tk.Button(button_frame, text="set",bg="blue",command=clear_text)
set_button.grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()
