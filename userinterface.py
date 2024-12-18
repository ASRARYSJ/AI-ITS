import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Intelligent Tutoring System")
root.configure(bg="#1a1a2e")  # Dark blue background color

# Add labels
label = tk.Label(root, text="Welcome to the ITS", font=("Helvetica", 20, "bold"), bg="#1a1a2e", fg="#ffffff")
label.pack(pady=20)

topic_label = tk.Label(root, text="Select a Topic:", font=("Helvetica", 16, "bold"), bg="#1a1a2e", fg="#ffffff")
topic_label.pack(pady=10)

# Dropdown for topics
topics = ["Algebra", "Geometry", "Calculus"]
topic_var = tk.StringVar(value=topics[0])
topic_menu = tk.OptionMenu(root, topic_var, *topics)
topic_menu.config(bg="#333333", fg="#ffffff", font=("Helvetica", 14), relief="flat")
topic_menu.pack(pady=15)

# Fetch content functionality
def fetch_content():
    selected_topic = topic_var.get()
    if selected_topic == "Algebra":
        content = """
        Algebra Content:
        - Solving Linear Equations
        - Quadratic Equations
        - Polynomials
        - Factoring Expressions
        - Exponents and Powers
        - Algebraic Fractions
        """
    else:
        content = f"Content for {selected_topic}"  # Placeholder for other topics

    messagebox.showinfo("Learning Content", content)

# Fetch button
button = tk.Button(root, text="Get Content", command=fetch_content, bg="#4CAF50", fg="#ffffff", font=("Helvetica", 14, "bold"), relief="raised", bd=3)
button.pack(pady=30)

root.mainloop()
