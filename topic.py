import tkinter as tk
from tkinter import ttk
t=''

def on_submit():
    topic = entry.get()
    result_label.config(text=f"You entered: {topic}")
    global t
    t=topic
    root.destroy()
# Create the main window
root = tk.Tk()
root.title("Topic Entry")
root.geometry("400x350")

# Create a frame for better organization
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Create the "Enter topic" label
label = ttk.Label(frame, text="Enter topic:", font=("Arial", 12))
label.pack(pady=10)

# Create the text entry box
entry = ttk.Entry(frame, width=30, font=("Arial", 11))
entry.pack(pady=10)
entry.focus()  # Set focus to the entry box when the app starts

# Create a submit button
submit_button = ttk.Button(frame, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Create a label to display the entered topic
result_label = ttk.Label(frame, text="", font=("Arial", 11))
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()