import tkinter as tk
from tkinter import messagebox

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Empower U - Login")
        self.geometry("800x600")  # Sets the initial window size
        self.create_widgets()

    def create_widgets(self):
        # Clear the window
        for widget in self.winfo_children():
            widget.destroy()

        # Create and place username label and entry
        label_username = tk.Label(self, text="Username")
        label_username.pack(pady=5)
        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)

        # Create and place password label and entry
        label_password = tk.Label(self, text="Password")
        label_password.pack(pady=5)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        # Create and place login button
        button_login = tk.Button(self, text="Login", command=self.login)
        button_login.pack(pady=10)

        # Create and place register button
        button_register = tk.Button(self, text="Register", command=self.open_register)
        button_register.pack(pady=10)

        # Create and place shut down button
        button_shutdown = tk.Button(self, text="Shut Down", command=self.quit)
        button_shutdown.pack(pady=10)

        # Create and place message label for login failure
        self.label_message = tk.Label(self, text="")
        self.label_message.pack(pady=5)

    def open_register(self):
        self.destroy()
        from interface.register import RegisterApp
        register_app = RegisterApp()
        register_app.mainloop()

    def load_user_data(self):
        users = []
        with open('user_data.txt', 'r') as file:
            for line in file:
                username, password, email, name = line.strip().split(',')
                users.append({
                    'username': username,
                    'password': password,
                    'email': email,
                    'name': name
                })
        return users

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        user_data = self.load_user_data()

        # Validate username and password
        for user in user_data:
            if user['username'] == username and user['password'] == password:
                self.clear_window()
                from interface.menu import show_main_menu
                show_main_menu(self)
                return

        # Display failure message
        self.label_message.config(text="Invalid username or password", fg="red")

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()