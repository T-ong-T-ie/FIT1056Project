# interface/menu.py
import tkinter as tk

def show_main_menu(root):
    root.clear_window()
    root.title("Empower U - Main Menu")
    root.geometry("800x600")  # Sets the initial window size

    # Create and place buttons for main menu
    button_auth = tk.Button(root, text="User Authentication")
    button_auth.pack(pady=10)

    button_progress = tk.Button(root, text="Progress Tracking")
    button_progress.pack(pady=10)

    button_tutorial = tk.Button(root, text="Interactive Tutorials", command=lambda: open_interactive_tutorials(root))
    button_tutorial.pack(pady=10)

    # Create and place logout button
    button_logout = tk.Button(root, text="Logout", command=lambda: logout(root))
    button_logout.pack(pady=10)

def open_interactive_tutorials(root):
    root.destroy()
    from interface.interactive_tutorials import InteractiveTutorialsApp
    tutorials_app = InteractiveTutorialsApp()
    tutorials_app.mainloop()

def logout(root):
    root.destroy()
    from interface.login import LoginApp
    login_app = LoginApp()
    login_app.mainloop()