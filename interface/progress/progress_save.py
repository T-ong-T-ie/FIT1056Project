import tkinter as tk
import os
from tkinter import messagebox
from interface.login import LoginApp


class LearningProgressTracker:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")  # Set the window size to 800x600
        self.progress_file = os.path.join("progress", "user_progress.txt")
        self.modules = {"Beginner": False, "Intermediate": False, "Advanced": False, "Quiz": False}
        self.load_progress()  # Load progress from the txt file
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()

        label_welcome = tk.Label(self.master, text="Welcome to EmpowerU Python Learning Platform")
        label_welcome.pack(pady=10)

        # Display each module and its completion status
        for module, completed in self.modules.items():
            status = "Completed" if completed else "Not Completed"
            label_module = tk.Label(self.master, text=f"{module}: {status}")
            label_module.pack(pady=5)

        # Button to show progress
        button_progress = tk.Button(self.master, text="Show Learning Progress", command=self.show_progress)
        button_progress.pack(pady=10)

        # Back to Main Menu button
        button_back = tk.Button(self.master, text="Back to Main Menu", command=self.back_to_main_menu)
        button_back.pack(pady=10)

    def show_progress(self):
        completed_modules = [module for module, completed in self.modules.items() if completed]
        total_modules = len(self.modules)
        completion_percentage = len(completed_modules) / total_modules * 100
        messagebox.showinfo("Learning Progress", f"You have completed {len(completed_modules)} out of {total_modules} modules ({completion_percentage:.2f}%).")

    def load_progress(self):
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as file:
                for line in file:
                    module, status = line.strip().split(": ")
                    self.modules[module] = True if status == "Completed" else False

    def back_to_main_menu(self):
        self.master.destroy()
        from interface.menu import show_main_menu
        main_menu_app = LoginApp()
        show_main_menu(main_menu_app)
        main_menu_app.mainloop()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()