import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")

        self.equation = tk.StringVar()
        self.entry_field = tk.Entry(self.root, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry_field.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        # Define button texts and grid positions
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("√", 5, 1), ("^", 5, 2), ("log", 5, 3),
            ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("exp", 6, 3),
            ("(", 7, 0), (")", 7, 1), ("pi", 7, 2), ("e", 7, 3)
        ]

        # Create buttons dynamically
        for (text, row, col) in buttons:
            if text == "=":
                button = tk.Button(self.root, text=text, padx=20, pady=20, command=self.calculate, font=('Arial', 18))
            elif text == "C":
                button = tk.Button(self.root, text=text, padx=20, pady=20, command=self.clear, font=('Arial', 18))
            else:
                button = tk.Button(self.root, text=text, padx=20, pady=20, command=lambda t=text: self.press(t), font=('Arial', 18))
            button.grid(row=row, column=col)

    def press(self, value):
        # Add button text to entry
        current = self.equation.get()
        if value == "pi":
            value = str(math.pi)
        elif value == "e":
            value = str(math.e)
        elif value == "√":
            value = "math.sqrt("
        elif value == "log":
            value = "math.log10("
        elif value == "sin":
            value = "math.sin(math.radians("
        elif value == "cos":
            value = "math.cos(math.radians("
        elif value == "tan":
            value = "math.tan(math.radians("
        self.equation.set(current + value)

    def calculate(self):
        try:
            result = eval(self.equation.get())  # Evaluate the expression
            self.equation.set(result)  # Update the entry with result
        except:
            self.equation.set("Error")  # Handle errors

    def clear(self):
        self.equation.set("")  # Clear the entry field

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
