import tkinter as tk
from tkinter import messagebox

class IntermediateTutorials:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()
        # Display the welcome message
        label_welcome = tk.Label(self.master, text="Welcome to EmpowerU Interactive Python Tutorial\nIn this tutorial, you will learn the basic knowledge about Python: variables, loops, and functions")
        label_welcome.pack(pady=10)

        # Create and place buttons for each tutorial section
        button_variables = tk.Button(self.master, text="Learn Variables", command=self.show_variables_tutorial)
        button_variables.pack(pady=10)

        button_loop = tk.Button(self.master, text="Learn Loops", command=self.show_loop_tutorial)
        button_loop.pack(pady=10)

        button_function = tk.Button(self.master, text="Learn Functions", command=self.show_function_tutorial)
        button_function.pack(pady=10)

        # Create and place back button
        button_back = tk.Button(self.master, text="Back to Learning Module Menu", command=self.back_to_learning_module_menu)
        button_back.pack(pady=10)

    def show_variables_tutorial(self):
        self.clear_window()

        label_variables = tk.Label(self.master, text="Variable tutorial started")
        label_variables.pack(pady=10)

        label_name = tk.Label(self.master, text="Please input your name, and your name will be variable 1:")
        label_name.pack(pady=5)
        self.entry_name = tk.Entry(self.master)
        self.entry_name.pack(pady=5)

        label_age = tk.Label(self.master, text="Please input your age, and your age will be variable 2:")
        label_age.pack(pady=5)
        self.entry_age = tk.Entry(self.master)
        self.entry_age.pack(pady=5)

        button_show = tk.Button(self.master, text="Show Variables", command=self.show_variables)
        button_show.pack(pady=10)

        button_back = tk.Button(self.master, text="Back to Intermediate Tutorial", command=self.create_widgets)
        button_back.pack(pady=10)

    def show_variables(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        messagebox.showinfo("Variables", f"Now, your information is {name}, {age}, which means variable1 + variable 2")

    def show_loop_tutorial(self):
        self.clear_window()

        label_loop = tk.Label(self.master, text="Loop tutorial started\n'while True' in Python means starting a loop, only when the input meets the conditions the loop will end\nLet us demonstrate it by a simple example")
        label_loop.pack(pady=10)

        label_animals = tk.Label(self.master, text="Let us create a list of your favorite animals")
        label_animals.pack(pady=5)
        self.entry_animal = tk.Entry(self.master)
        self.entry_animal.pack(pady=5)

        self.animals = []

        button_add = tk.Button(self.master, text="Add Animal", command=self.add_animal)
        button_add.pack(pady=10)

        button_back = tk.Button(self.master, text="Back to Intermediate Tutorial", command=self.create_widgets)
        button_back.pack(pady=10)

    def add_animal(self):
        animal = self.entry_animal.get()
        if animal.lower() == "finish":
            messagebox.showinfo("Favorite Animals", f"Your favorite animals are: {self.animals}")
        else:
            self.animals.append(animal)
            self.entry_animal.delete(0, tk.END)

    def show_function_tutorial(self):
        self.clear_window()

        label_function = tk.Label(self.master, text="Now let us create a simple function to list your information")
        label_function.pack(pady=10)

        label_name = tk.Label(self.master, text="Please input your name:")
        label_name.pack(pady=5)
        self.entry_name = tk.Entry(self.master)
        self.entry_name.pack(pady=5)

        label_age = tk.Label(self.master, text="Please input your age:")
        label_age.pack(pady=5)
        self.entry_age = tk.Entry(self.master)
        self.entry_age.pack(pady=5)

        button_show = tk.Button(self.master, text="Show Information", command=self.show_information)
        button_show.pack(pady=10)

        button_back = tk.Button(self.master, text="Back to Intermediate Tutorial", command=self.create_widgets)
        button_back.pack(pady=10)

    def show_information(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        messagebox.showinfo("Information", f"Your name is {name} and you are {age} years old")

    def back_to_learning_module_menu(self):
        self.master.clear_window()
        self.master.create_widgets()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()