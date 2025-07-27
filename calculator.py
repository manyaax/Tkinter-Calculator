import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Calculator")
        self.root.geometry("400x550")  # Bigger, fixed size
        self.root.resizable(False, False)

        self.expression = ""
        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        self.display = tk.Entry(self.root, font=("Arial", 28), bd=10, relief=tk.RIDGE, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, padx=10, pady=15, sticky="we")
        self.display.configure(state="readonly")

        # Define all buttons
        buttons = [
            ('C', 1, 0), ('←', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(
                self.root, text=text, width=5, height=2,
                font=("Arial", 20), bd=4,
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

        # Make all rows and columns expand equally
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def bind_keys(self):
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<Return>", lambda event: self.evaluate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            self.evaluate()
            return
        elif char == "←":
            self.backspace()
        elif char == "+/-":
            self.toggle_sign()
        elif char == "%":
            self.handle_percentage()
        else:
            self.expression += str(char)

        self.update_display()

    def on_key_press(self, event):
        char = event.char
        if char in "0123456789+-*/.%":
            self.expression += char
            self.update_display()
        elif event.keysym == "Escape":
            self.expression = ""
            self.update_display()

    def update_display(self):
        self.display.configure(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)
        self.display.configure(state="readonly")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def toggle_sign(self):
        try:
            if self.expression:
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
                self.update_display()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def handle_percentage(self):
        try:
            if self.expression:
                value = eval(self.expression) / 100
                self.expression = str(value)
                self.update_display()
        except:
            self.expression = "Error"
            self.update_display()

    def evaluate(self):
        try:
            if not self.expression:
                return
            result = eval(self.expression)
            self.expression = str(result)
        except ZeroDivisionError:
            self.expression = "Error: DivBy0"
        except:
            self.expression = "Error"
        self.update_display()


# Run the Calculator
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
