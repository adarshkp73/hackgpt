import tkinter as tk
from tkinter import scrolledtext
import gemini
from google import genai
from google.genai import types
import mcq

score=mcq.score1
t=mcq.t
print('Please wait, Loading!')

history=[types.Content(role="user",parts=[types.Part.from_text(text=f'i have a score of {score}/20 in {t}, explain the topic in accordance with the score'),],)]
out=gemini.generate(history)
history+=[types.Content(role="model",parts=[types.Part.from_text(text=out)])]
x=1

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Interface")
        self.root.geometry("500x400")
        self.root.resizable(True, True)
        
        # Create frame for input area
        input_frame = tk.Frame(root)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Create input text box
        self.input_box = scrolledtext.ScrolledText(input_frame, height=5, wrap=tk.WORD)
        self.input_box.pack(fill=tk.X, side=tk.LEFT, expand=True)
        
        # Create send button
        send_button = tk.Button(input_frame, text="Send", width=10, command=self.send_message)
        send_button.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Create output area
        output_frame = tk.Frame(root)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Label for output
        output_label = tk.Label(output_frame, text="Output:")
        output_label.pack(anchor=tk.W)
        
        # Create output text box
        self.output_box = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD)
        self.output_box.pack(fill=tk.BOTH, expand=True)
        global history, x, out
        if x==1:
            #self.output_box.config(state=tk.NORMAL)
            self.output_box.insert(tk.END, f"Model: {out}\n\n")
            self.output_box.config(state=tk.DISABLED)
            self.output_box.see(tk.END)
            x+=1
        
        # Configure output box to be read-only
        #self.output_box.config(state=tk.DISABLED)
        
    def send_message(self):
        # Get the input text
        message = self.input_box.get("1.0", tk.END).strip()
        global history
        '''if x==1:
            self.output_box.config(state=tk.NORMAL)
            self.output_box.insert(tk.END, f"Model: {out}\n\n")
            self.output_box.config(state=tk.DISABLED)
            self.output_box.see(tk.END)
            x+=1'''

        if message:
            # Enable output box for editing
            self.output_box.config(state=tk.NORMAL)
            
            # Add message to output box
            self.output_box.insert(tk.END, f"You: {message}\n\n")

            history+=[types.Content(role="user",parts=[types.Part.from_text(text=message)])]
            s=gemini.generate(history)
            history+=[types.Content(role="model",parts=[types.Part.from_text(text=s)])]
            self.output_box.insert(tk.END, f"AthenAI: {s}\n\n")

            # Clear input box
            self.input_box.delete("1.0", tk.END)
            
            # Disable output box for editing
            self.output_box.config(state=tk.DISABLED)
            
            # Auto-scroll to the end of output
            self.output_box.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
    