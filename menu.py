import tkinter as tk

def show_main_menu():
    root = tk.Tk()
    root.title("Empower U - Main Menu")

    # Create and place buttons for main menu
    button_auth = tk.Button(root, text="User Authentication")
    button_auth.pack(pady=10)

    button_progress = tk.Button(root, text="Progress Tracking")
    button_progress.pack(pady=10)

    button_tutorial = tk.Button(root, text="Interactive Tutorials")
    button_tutorial.pack(pady=10)

    root.mainloop()