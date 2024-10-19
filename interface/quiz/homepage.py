import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, master):
        """
        Constructor for the HomePage class.
        """
        super().__init__(master)
        self.master = master

        # Buttons for different learning topics
        self.python_button = tk.Button(self, text="Test You Python Knowledge", command=self.go_to_python)
        self.python_button.grid(row=0, column=0, padx=10, pady=10)

        self.info_sec_button = tk.Button(self, text="Test You Information Security Knowledge", command=self.go_to_info_sec)
        self.info_sec_button.grid(row=1, column=0, padx=10, pady=10)

        self.ai_button = tk.Button(self, text="Test You Artificial Intelligence Knowledge", command=self.go_to_ai)
        self.ai_button.grid(row=2, column=0, padx=10, pady=10)

        self.profile_button = tk.Button(self, text="Learner's Profile")
        self.profile_button.grid(row=3, column=0, padx=10, pady=10)

        self.shutdown_button = tk.Button(self, text="Shut down", command=master.destroy)
        self.shutdown_button.grid(row=4, column=0, padx=10, pady=10)

    def go_to_python(self):
        """
        Method to switch to Python learning content.
        """
        self.master.python_content()

    def go_to_info_sec(self):
        """
        Method to switch to Information Security content.
        """
        self.master.info_sec_content()

    def go_to_ai(self):
        """
        Method to switch to Artificial Intelligence content.
        """
        self.master.ai_content()