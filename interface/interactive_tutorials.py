# interface/interactive_tutorials.py
import tkinter as tk
from tkinter import messagebox
import subprocess

class InteractiveTutorialsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Empower U - Interactive Tutorials")
        self.geometry("800x600")  # 设置窗口初始大小
        self.create_widgets()

    def create_widgets(self):
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
        button_back = tk.Button(self, text="Back to Main Menu", command=self.back_to_main_menu)
        button_back.pack(pady=10)

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

    def back_to_main_menu(self):
        self.destroy()
        from interface.menu import show_main_menu
        show_main_menu()