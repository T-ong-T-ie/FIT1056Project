import tkinter as tk

def show_main_menu():
    root = tk.Tk()
    root.title("Empower U - Main Menu")
    root.geometry("400x300")  # 设置窗口初始大小

    # Create and place buttons for main menu
    button_auth = tk.Button(root, text="User Authentication")
    button_auth.pack(pady=10)

    button_progress = tk.Button(root, text="Progress Tracking")
    button_progress.pack(pady=10)

    button_tutorial = tk.Button(root, text="Interactive Tutorials")
    button_tutorial.pack(pady=10)

    # Create and place shut down button
    button_shutdown = tk.Button(root, text="Shut Down", command=root.quit)
    button_shutdown.pack(pady=10)

    root.mainloop()