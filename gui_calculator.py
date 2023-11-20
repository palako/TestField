import tkinter as tk
from calculator import Calculator


class GUI_Calculator:
    def __init__(self):
        self.calc = Calculator()
        self.main_window = tk.Tk()
        self.main_window.title('Calculator')

        self.create_widgets()

    def create_widgets(self):
        self.buttons_frame = tk.Frame(self.main_window)
        self.buttons_frame.grid(row=0, column=0, sticky='nsew')

        self.button_texts = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '0', 'C', '/', '=',
            'sqrt'
        ]

        self.buttons = {}
        for index, text in enumerate(self.button_texts):
            command = lambda text=text: self.button_clicked(text)
            self.buttons[text] = tk.Button(self.buttons_frame, text=text, command=command, bg='orange')
            row, col = divmod(index, 4)
            self.buttons[text].grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

        for i in range(5):
            self.buttons_frame.columnconfigure(i, weight=1)
            self.buttons_frame.rowconfigure(i, weight=1)

        self.display = tk.Entry(self.main_window, justify='right')
        self.display.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

    def button_clicked(self, value):
        if value in '0123456789':
            self.append_display(value)
        elif value == 'C':
            self.clear_display()
        elif value in '+-*/':
            self.append_operator(value)
        elif value == '=':
            self.calculate_result()
        elif value == 'sqrt':
            self.calculate_square_root()

    def append_display(self, value):
        self.display.insert(tk.END, value)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def append_operator(self, operator):
        self.display.insert(tk.END, operator)

    def calculate_result(self):
        expression = self.display.get()
        try:
            result = eval(expression, {'__builtins__': None}, {'Calculator': Calculator, 'calc': self.calc})
            self.clear_display()
            self.display.insert(tk.END, str(result))
        except Exception as error:
            self.clear_display()
            self.display.insert(tk.END, 'Error')

    def calculate_square_root(self):
        expression = self.display.get()
        try:
            alpha = float(expression)
            result = self.calc.f_square_root(alpha)
            self.clear_display()
            self.display.insert(tk.END, str(result))
        except Exception as error:
            self.clear_display()
            self.display.insert(tk.END, 'Error')

    def run(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    gui_calc = GUI_Calculator()
    gui_calc.run()
