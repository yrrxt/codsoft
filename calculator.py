import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Entry for displaying the expression and result
        self.entry = ttk.Entry(root, width=30, font=('Helvetica', 20), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons for numbers
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('0', 4, 0, columnspan=2)

        # Buttons for operators
        self.create_button('+', 1, 3)
        self.create_button('-', 2, 3)
        self.create_button('*', 3, 3)
        self.create_button('/', 4, 3)

        # Equal and clear button
        self.create_button('=', 4, 2)
        self.create_button('C', 4, 1)

        # Bind keys for keyboard input
        self.root.bind('<Key>', self.key_pressed)

        # Initialize expression and result variables
        self.expression = ""
        self.result = ""

    def create_button(self, text, row, column, columnspan=1, padx=10, pady=10):
        button = ttk.Button(self.root, text=text, width=7, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady)

    def button_click(self, text):
        if text == '=':
            try:
                self.result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, self.result)
                self.expression = self.result
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        elif text == 'C':
            self.entry.delete(0, tk.END)
            self.expression = ""
        else:
            self.expression += text
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def key_pressed(self, event):
        if event.char.isdigit() or event.char in ['+', '-', '*', '/', '=']:
            self.button_click(event.char)
        elif event.keysym == 'Return':
            self.button_click('=')
        elif event.keysym == 'BackSpace':
            self.expression = self.expression[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
