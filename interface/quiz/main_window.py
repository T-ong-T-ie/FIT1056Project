import tkinter as tk
from tkinter import messagebox
from interface.quiz.homepage import HomePage

class EMPOWERU(tk.Tk):
    def __init__(self, title, width, height):
        """
        Constructor for the EMPOWERU class.

        Parameter(s):
        - title: str
        - width: int, width of window in pixels
        - height: int, height of window in pixels
        """
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")

        # Initialize homepage and show it initially
        self.homepage = HomePage(master=self)
        self.show_homepage()

        self.current_subject = None  # Track which subject is active (Python, InfoSec, AI)

    def show_homepage(self):
        """
        Displays the home page to make it visible in the main window.
        """
        self.clear_content()  # Clear any other displayed content
        self.homepage.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_homepage(self):
        """
        Hides the home page to make it invisible in the main window.
        """
        self.homepage.place_forget()

    def python_content(self):
        """
        Displays Python content in the main window, hiding any previous content.
        """
        self.hide_homepage()
        self.clear_content()
        self.current_subject = "Python"

        # Display Python content
        self.label = tk.Label(
            self,
            text=(
                "**Python Learning Material**\n\n"
                "Python is a versatile programming language known for its readability and broad library support. "
                "It is widely used in web development, data analysis, artificial intelligence, and more."
            ),
            wraplength=600,
            justify="left",
        )
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="w")

        self.quiz_button = tk.Button(self, text="Go to Python Quiz", command=self.show_quiz)
        self.quiz_button.grid(row=1, column=0, padx=10, pady=10)

        # Back button to return to the homepage
        self.back_button = tk.Button(self, text="Go Back", command=self.show_homepage)
        self.back_button.grid(row=1, column=1, padx=10, pady=10)

    def info_sec_content(self):
        """
        Displays Information Security content in the main window, hiding any previous content.
        """
        self.hide_homepage()
        self.clear_content()
        self.current_subject = "Information Security"

        # Display Information Security content
        self.label = tk.Label(
            self,
            text=(
                "**Information Security Learning Material**\n\n"
                "Information Security involves protecting information and information systems from unauthorized "
                "access, use, disclosure, disruption, modification, or destruction to provide confidentiality, "
                "integrity, and availability."
            ),
            wraplength=600,
            justify="left",
        )
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="w")

        self.quiz_button = tk.Button(self, text="Go to InfoSec Quiz", command=self.show_quiz)
        self.quiz_button.grid(row=1, column=0, padx=10, pady=10)

        # Back button to return to the homepage
        self.back_button = tk.Button(self, text="Go Back", command=self.show_homepage)
        self.back_button.grid(row=1, column=1, padx=10, pady=10)

    def ai_content(self):
        """
        Displays Artificial Intelligence content in the main window, hiding any previous content.
        """
        self.hide_homepage()
        self.clear_content()
        self.current_subject = "Artificial Intelligence"

        # Display AI content
        self.label = tk.Label(
            self,
            text=(
                "**Artificial Intelligence Learning Material**\n\n"
                "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, "
                "especially computer systems. These processes include learning, reasoning, and self-correction."
            ),
            wraplength=600,
            justify="left",
        )
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="w")

        self.quiz_button = tk.Button(self, text="Go to AI Quiz", command=self.show_quiz)
        self.quiz_button.grid(row=1, column=0, padx=10, pady=10)

        # Back button to return to the homepage
        self.back_button = tk.Button(self, text="Go Back", command=self.show_homepage)
        self.back_button.grid(row=1, column=1, padx=10, pady=10)

    def show_quiz(self):
        """
        Displays a quiz related to the current subject.
        """
        self.clear_content()
        if self.current_subject == "Python":
            self.display_mcq(quiz="python")
        elif self.current_subject == "Information Security":
            self.display_mcq(quiz="infosec")
        elif self.current_subject == "Artificial Intelligence":
            self.display_mcq(quiz="ai")

    def display_mcq(self, quiz):
        """
        Display multiple-choice questions based on the selected quiz.
        """
        questions = {
            "python": [
                ("What is the correct file extension for Python files?", [".py", ".python", ".pt", ".pyt"]),
                ("Which keyword is used to create a function in Python?", ["function", "def", "fun", "define"]),
                ("Which of the following is a mutable data type in Python?", ["tuple", "list", "string", "int"]),
            ],
            "infosec": [
                ("What does 'CIA' stand for in Information Security?", ["Confidentiality, Integrity, Availability", "Control, Integrity, Access", "Confidentiality, Identity, Authentication", "Confidentiality, Information, Access"]),
                ("Which of these is a common type of cyber attack?", ["Phishing", "Farming", "Grazing", "Sowing"]),
                ("A firewall is used to:", ["Filter network traffic", "Store data", "Encrypt data", "Authenticate users"]),
            ],
            "ai": [
                ("Which of these is a subset of AI that focuses on learning from data?", ["Machine Learning", "Data Mining", "Computer Vision", "Robotics"]),
                ("What is the term for a network model inspired by the human brain?", ["Neural Network", "Decision Tree", "Support Vector Machine", "Linear Regression"]),
                ("In AI, what does 'NLP' stand for?", ["Natural Language Processing", "Neural Link Protocol", "Network Layer Processing", "New Learning Paradigm"]),
            ],
        }

        quiz_questions = questions.get(quiz, [])

        self.vars = []  # Store the variables for each question's answer
        for i, (question, options) in enumerate(quiz_questions):
            # Display question
            question_label = tk.Label(self, text=f"Q{i+1}: {question}", wraplength=600, justify="left")
            question_label.grid(row=i*5, column=0, columnspan=2, padx=20, pady=5, sticky="w")

            # Variable to store user's answer
            var = tk.StringVar(value="")

            # Display options
            for j, option in enumerate(options):
                option_button = tk.Radiobutton(self, text=option, variable=var, value=option)
                option_button.grid(row=i*5 + j + 1, column=0, sticky="w", padx=40)

            self.vars.append((var, options[0]))  # Store the variable and correct answer

        # Submit button
        submit_button = tk.Button(self, text="Submit Answers", command=self.submit_answers)
        submit_button.grid(row=len(quiz_questions)*5, column=0, padx=10, pady=20)

        # Back button to return to the content
        back_button = tk.Button(self, text="Go Back", command=self.go_back_to_content)
        back_button.grid(row=len(quiz_questions)*5, column=1, padx=10, pady=20)

    def submit_answers(self):
        """
        Handles submission of quiz answers.
        """
        score = 0
        total = len(self.vars)
        for var, correct_answer in self.vars:
            if var.get() == correct_answer:
                score += 1

        messagebox.showinfo("Quiz Results", f"You scored {score} out of {total}.")

        # Return to content after submitting
        self.go_back_to_content()

    def go_back_to_content(self):
        """
        Returns to the content screen based on the current subject.
        """
        if self.current_subject == "Python":
            self.python_content()
        elif self.current_subject == "Information Security":
            self.info_sec_content()
        elif self.current_subject == "Artificial Intelligence":
            self.ai_content()

    def clear_content(self):
        """
        Utility method to clear any existing content in the window.
        This helps when switching between different screens.
        """
        for widget in self.winfo_children():
            widget.grid_forget()