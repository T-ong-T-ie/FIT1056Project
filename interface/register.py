# interface/register.py
import tkinter as tk
from tkinter import messagebox

class RegisterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Empower U - Register")
        self.geometry("800x600")  # 设置窗口初始大小
        self.create_widgets()

    def create_widgets(self):
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

        # Create and place email label and entry
        label_email = tk.Label(self, text="Email")
        label_email.pack(pady=5)
        self.entry_email = tk.Entry(self)
        self.entry_email.pack(pady=5)

        # Create and place name label and entry
        label_name = tk.Label(self, text="Name")
        label_name.pack(pady=5)
        self.entry_name = tk.Entry(self)
        self.entry_name.pack(pady=5)

        # Create and place register button
        button_register = tk.Button(self, text="Register", command=self.register)
        button_register.pack(pady=10)

        # Create and place cancel button
        button_cancel = tk.Button(self, text="Cancel", command=self.cancel)
        button_cancel.pack(pady=10)

        # Create and place shut down button
        button_shutdown = tk.Button(self, text="Shut Down", command=self.quit)
        button_shutdown.pack(pady=10)

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        email = self.entry_email.get()
        name = self.entry_name.get()

        if not username or not password or not email or not name:
            messagebox.showerror("Error", "All fields are required")
            return

        with open('user_data.txt', 'a') as file:
            file.write(f"{username},{password},{email},{name}\n")

        messagebox.showinfo("Register", "Registration successful!")
        self.destroy()
        from interface.login import LoginApp
        login_app = LoginApp()
        login_app.mainloop()

    def cancel(self):
        self.destroy()
        from interface.login import LoginApp
        login_app = LoginApp()
        login_app.mainloop()