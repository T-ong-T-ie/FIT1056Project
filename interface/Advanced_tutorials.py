import tkinter as tk
from tkinter import messagebox

class AdvancedTutorials:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()
        # Display the welcome message
        label_welcome = tk.Label(self.master, text="Welcome to EmpowerU Advanced Python Tutorial\nIn this tutorial, you will learn advanced topics: File Handling, OOP, Exception Handling, and Modules")
        label_welcome.pack(pady=10)

        # Create and place buttons for each tutorial section
        button_file_handling = tk.Button(self.master, text="Learn File Handling", command=self.show_file_handling_tutorial)
        button_file_handling.pack(pady=10)

        button_oop = tk.Button(self.master, text="Learn Object-Oriented Programming", command=self.show_oop_tutorial)
        button_oop.pack(pady=10)

        button_exceptions = tk.Button(self.master, text="Learn Exception Handling", command=self.show_exceptions_tutorial)
        button_exceptions.pack(pady=10)

        button_modules = tk.Button(self.master, text="Learn Modules", command=self.show_modules_tutorial)
        button_modules.pack(pady=10)

        # Create and place back button
        button_back = tk.Button(self.master, text="Back to Learning Module Menu", command=self.back_to_learning_module_menu)
        button_back.pack(pady=10)

    def show_file_handling_tutorial(self):
        self.clear_window()

        label_file = tk.Label(self.master, text="File Handling tutorial started\nYou will learn how to read and write files in Python")
        label_file.pack(pady=10)

        label_filename = tk.Label(self.master, text="Enter the filename to create a new file:")
        label_filename.pack(pady=5)
        self.entry_filename = tk.Entry(self.master)
        self.entry_filename.pack(pady=5)

        label_content = tk.Label(self.master, text="Enter content for the file:")
        label_content.pack(pady=5)
        self.entry_content = tk.Entry(self.master)
        self.entry_content.pack(pady=5)

        button_create_file = tk.Button(self.master, text="Create File", command=self.create_file)
        button_create_file.pack(pady=10)

        button_back = tk.Button(self.master, text="Back to Advanced Tutorial", command=self.create_widgets)
        button_back.pack(pady=10)

    def create_file(self):
        filename = self.entry_filename.get()
        content = self.entry_content.get()
        try:
            with open(filename, 'w') as file:
                file.write(content)
            messagebox.showinfo("File Handling", f"File '{filename}' created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def show_oop_tutorial(self):
        self.clear_window()

        label_oop = tk.Label(self.master, text="Object-Oriented Programming (OOP) tutorial started\nYou will learn how to create classes and objects in Python")
        label_oop.pack(pady=10)

        label_class_name = tk.Label(self.master, text="Enter a class name to create:")
        label_class_name.pack(pady=5)
        self.entry_class_name = tk.Entry(self.master)
        self.entry_class_name.pack(pady=5)

        button_create_class = tk.Button(self.master, text="Create Class", command=self.create_class)
        button_create_class.pack(pady=10)

        button_back = tk.Button(self.master, text="Back to Advanced Tutorial", command=self.create_widgets)
        button_back.pack(pady=10)

    def create_class(self):
        class_name = self.entry_class_name.get()
        class_template = f"class {class_name}:\n    def __init__(self, attribute):\n        self.attribute = attribute\n\n    def show_attribute(self):\n        return self.attribute"
        messagebox.showinfo("OOP", f"Here is a simple class:\n\n{class_template}")

    def show_exceptions_tutorial(self):
        self.clear_window()

        label_exceptions = tk.Label(self.master, text="Exception Handling tutorial started\nYou will learn how to handle errors using try, except, and finally")
        label_exceptions.pack(pady=10)

        button_example = tk.Button(self.master, text="Show Example", command=self.show_exception_example)
        button_example.pack(pady=10)

        button_back = tk.Button(self.master, text="Back to Advanced Tutorial", command=self.create_widgets)
        button_back.pack(pady=10)

    def show_exception_example(self):
        try:
            x = int("not a number")
        except ValueError as e:
            messagebox.showerror("Exception Handling", f"A ValueError occurred: {e}")
        finally:
            messagebox.showinfo("Exception Handling", "This block of code will always execute, even if an error occurs.")

    def show_modules_tutorial(self):
        self.clear_window()

        label_modules = tk.Label(self.master, text="Modules tutorial started\nYou will learn how to import and use Python modules")
        label_modules.pack(pady=10)

        button_example = tk.Button(self.master, text="Show Module Example", command=self.show_module_example)
        button_example.pack(pady=10)

        button_back = tk.Button(self.master, text="Back to Advanced Tutorial", command=self.create_widgets)
        button_back.pack(pady=10)

    def show_module_example(self):
        import math
        pi_value = math.pi
        messagebox.showinfo("Modules", f"Example of using a module: math.pi = {pi_value}")

    def back_to_learning_module_menu(self):
        self.master.clear_window()
        self.master.create_widgets()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()