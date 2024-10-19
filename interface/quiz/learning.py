import tkinter as tk

class LearningContent(tk.Frame):
    def __init__(self, master):
        """
        Constructor for the LearningContent class.
        """
        super().__init__(master=master)
        self.master = master

        # Button to show chapter 1 content
        self.chapter1_btn = tk.Button(self, text="Chapter 1", command=self.show_chapter1)
        self.chapter1_btn.pack(padx=10, pady=10)

        # Button to go back to the homepage
        self.back_btn = tk.Button(self, text="Go Back", command=self.hide_menu)
        self.back_btn.pack(padx=10, pady=10)

    def hide_menu(self):
        """
        Hides the current menu and returns to the homepage.
        """
        self.place_forget()
        self.master.show_homepage()

    def show_chapter1(self):
        """
        Shows the content for chapter 1.
        """
        self.place_forget()
        self.master.python_content()