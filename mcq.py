import tkinter as tk
from tkinter import messagebox
import questions
import topic

t=topic.t
print('Please wait, Loading!')
score1=0

class MCQApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz Application")
        self.root.geometry("700x500")
        self.root.config(bg="#ffffff")
        
        self.current_question = 0
        self.score = 0
        self.selected_option = tk.StringVar()
        self.questions = []
        
        # Header
        header_frame = tk.Frame(root, bg="#ffffff")
        header_frame.pack(fill=tk.X)
        
        header_label = tk.Label(
            header_frame, 
            text="Multiple Choice Quiz", 
            font=("Arial", 18, "bold"), 
            bg="#ffffff", 
            fg="white",
            pady=10
        )
        header_label.pack()
        
        # Question Frame
        self.question_frame = tk.Frame(root, bg="#ffffff", pady=20)
        self.question_frame.pack(fill=tk.BOTH, expand=True)
        
        self.question_label = tk.Label(
            self.question_frame,
            text="",
            font=("Arial", 14),
            bg="#ffffff",
            wraplength=650,
            justify=tk.LEFT,
            pady=10
        )
        self.question_label.pack(anchor=tk.W, padx=20)
        
        # Options Frame
        self.options_frame = tk.Frame(self.question_frame, bg="#ffffff")
        self.options_frame.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Create option radio buttons
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected_option,
                value=str(i),
                font=("Arial", 12),
                bg="#ffffff",
                wraplength=600,
                justify=tk.LEFT,
                pady=5
            )
            rb.pack(anchor=tk.W, pady=5)
            self.option_buttons.append(rb)
        
        # Navigation buttons
        button_frame = tk.Frame(root, bg="#ffffff", pady=10)
        button_frame.pack(fill=tk.X)
        
        self.next_button = tk.Button(
            button_frame,
            text="Next",
            command=self.next_question,
            font=("Arial", 12),
            bg="#ffffff",
            fg="black",
            padx=20,
            pady=5
        )
        self.next_button.pack(side=tk.RIGHT, padx=20)
        
        self.prev_button = tk.Button(
            button_frame,
            text="Previous",
            command=self.prev_question,
            font=("Arial", 12),
            bg="#ffffff",
            fg="black",
            padx=20,
            pady=5,
            state=tk.DISABLED
        )
        self.prev_button.pack(side=tk.LEFT, padx=20)
    
    def add_question(self, question_text, options, correct_answer):
        """Add a question to the quiz."""
        self.questions.append({
            "question": question_text,
            "options": options,
            "correct_answer": correct_answer,
            "user_answer": None
        })
    
    def display_question(self):
        """Display the current question."""
        if not self.questions:
            self.question_label.config(text="No questions available.")
            return
        
        question = self.questions[self.current_question]
        self.question_label.config(text=f"Q{self.current_question + 1}: {question['question']}")
        
        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=f"{chr(65 + i)}. {option}")
            self.option_buttons[i].config(value=str(i))
        
        # Set the previously selected answer if any
        if question["user_answer"] is not None:
            self.selected_option.set(str(question["user_answer"]))
        else:
            self.selected_option.set("")
        
        # Update button states
        if self.current_question == 0:
            self.prev_button.config(state=tk.DISABLED)
        else:
            self.prev_button.config(state=tk.NORMAL)
        
        if self.current_question == len(self.questions) - 1:
            self.next_button.config(text="Finish")
        else:
            self.next_button.config(text="Next")
    
    def next_question(self):
        """Move to the next question or finish the quiz."""
        # Save the current answer
        if self.selected_option.get():
            self.questions[self.current_question]["user_answer"] = int(self.selected_option.get())
        
        if self.current_question == len(self.questions) - 1:
            # This is the last question, show results
            self.show_results()
            return
        
        self.current_question += 1
        self.display_question()
    
    def prev_question(self):
        """Move to the previous question."""
        # Save the current answer
        if self.selected_option.get():
            self.questions[self.current_question]["user_answer"] = int(self.selected_option.get())
        
        self.current_question -= 1
        self.display_question()
    
    def show_results(self):
        """Calculate score and show results."""
        # Calculate score
        self.score = 0
        for q in self.questions:
            if q["user_answer"] == q["correct_answer"]:
                self.score += 1
        global score1
        score1=self.score
        
        result_message = f"You scored {self.score} out of {len(self.questions)}"
        messagebox.showinfo("Quiz Results", result_message)
        
        # Option to restart or exit
        '''if messagebox.askyesno("Quiz Complete", "Do you want to restart the quiz?"):
            # Reset user answers
            for q in self.questions:
                q["user_answer"] = None
            self.current_question = 00
            self.display_question()
        else:'''
        self.root.destroy()
    
    def start_quiz(self):
        """Start the quiz by displaying the first question."""
        if self.questions:
            self.display_question()
        else:
            messagebox.showerror("Error", "No questions available. Please add questions first.")


# Example usage:
#if __name__ == "__main__":
root = tk.Tk()
app = MCQApp(root)

qs= questions.generate(t)
for i in range(2):
        #question, answers, correct_ans = backend.get_questions(questions.generate('thermodynamics for chemistry'), i)
        question, answers,correct_ans=qs[i]
        app.add_question(
        f"{question}",
        answers,
        correct_ans  #index of correct option
        )
    
    # Start the quiz
app.start_quiz()
root.mainloop()
