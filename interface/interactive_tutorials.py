import tkinter as tk
from tkinter import messagebox
import subprocess
from interface.Intermediate_tutorials import IntermediateTutorials
from interface.Advanced_tutorials import AdvancedTutorials
from interface.quiz.main_window import EMPOWERU

class InteractiveTutorialsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Empower U - Interactive Tutorials")
        self.geometry("800x600")  # Sets the initial window size
        self.create_widgets()

    def create_widgets(self):
        # Create and place module buttons and descriptions
        button_beginner = tk.Button(self, text="Beginner Module", command=self.show_tutorial)
        button_beginner.pack(pady=5)
        label_beginner = tk.Label(self, text="Beginner module: suitable for beginners, providing basic knowledge.")
        label_beginner.pack(pady=5)

        button_intermediate = tk.Button(self, text="Intermediate Module", command=self.show_intermediate_tutorial)
        button_intermediate.pack(pady=5)
        label_intermediate = tk.Label(self, text="Intermediate module: for learners with some basics, teaching advanced skills.")
        label_intermediate.pack(pady=5)

        button_advanced = tk.Button(self, text="Advanced Module", command=self.show_advanced_tutorial)
        button_advanced.pack(pady=5)
        label_advanced = tk.Label(self, text="Advanced module: for experienced users, teaching complex concepts and practical applications.")
        label_advanced.pack(pady=5)

        # Create and place Quiz button
        button_quiz = tk.Button(self, text="Quiz", command=self.open_quiz)
        button_quiz.pack(pady=10)

        # Create and place back button
        button_back = tk.Button(self, text="Back to Main Menu", command=self.back_to_main_menu)
        button_back.pack(pady=10)

    def show_tutorial(self):
        # Clear the window
        for widget in self.winfo_children():
            widget.destroy()

        # Add a brief introduction to Python
        label_intro = tk.Label(self, text="Welcome to the Beginner Module!\nPython is a versatile programming language used for various applications.\nLet's start with a simple program to print 'hello world'.")
        label_intro.pack(pady=10)

        # Create and place code input text area
        label_code_input = tk.Label(self, text="Enter your Python code:")
        label_code_input.pack(pady=5)
        self.text_code_input = tk.Text(self, height=15, width=70)
        self.text_code_input.pack(pady=5)

        # Create and place run button
        button_run = tk.Button(self, text="Run Code", command=self.run_code)
        button_run.pack(pady=10)

        # Create and place output text area
        label_output = tk.Label(self, text="Output:")
        label_output.pack(pady=5)
        self.text_output = tk.Text(self, height=10, width=70, state=tk.DISABLED)
        self.text_output.pack(pady=5)

        # Create and place back button
        button_back = tk.Button(self, text="Back to Learning Module Menu", command=self.back_to_learning_module_menu)
        button_back.pack(pady=10)

    def show_intermediate_tutorial(self):
        # Clear the window
        for widget in self.winfo_children():
            widget.destroy()

        # Initialize and display the intermediate tutorials
        IntermediateTutorials(self)

    def show_advanced_tutorial(self):
        # Clear the window
        for widget in self.winfo_children():
            widget.destroy()

        # Initialize and display the advanced tutorials
        AdvancedTutorials(self)

    def run_code(self):
        code = self.text_code_input.get("1.0", tk.END)
        try:
            # Save the code to a temporary file
            with open("temp_code.py", "w") as file:
                file.write(code)

            # Run the code and capture the output
            result = subprocess.run(["python", "temp_code.py"], capture_output=True, text=True)
            output = result.stdout + result.stderr

            # Display the output
            self.text_output.config(state=tk.NORMAL)
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, output)
            self.text_output.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_quiz(self):
        self.destroy()
        quiz_app = EMPOWERU(title="EMPOWERU Quiz", width=800, height=600)
        quiz_app.mainloop()

    def back_to_main_menu(self):
        self.clear_window()
        from interface.menu import show_main_menu
        show_main_menu(self)

    def back_to_learning_module_menu(self):
        self.clear_window()
        self.create_widgets()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()