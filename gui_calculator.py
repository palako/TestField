import tkinter as tk
from calculator import Calculator


class f_GUI_Calculator:
    def __init__(f_self):
        f_self.calc = Calculator()
        f_self.main_window = tk.Tk()
        f_self.main_window.title('Calculator')

        f_self.f_create_widgets()

    def f_create_widgets(f_self):
        f_self.buttons_frame = tk.Frame(f_self.main_window)
        f_self.buttons_frame.grid(row=0, column=0, sticky='nsew')

        f_self.button_texts = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '0', 'C', '/', '=',
            'sqrt'
        ]

        f_self.buttons = {}
        for f_index, f_text in enumerate(f_self.button_texts):
            f_command = lambda f_text=f_text: f_self.f_button_clicked(f_text)
            f_self.buttons[f_text] = tk.Button(f_self.buttons_frame, text=f_text, command=f_command, bg='orange')
            f_row, f_col = divmod(f_index, 4)
            f_self.buttons[f_text].grid(row=f_row, column=f_col, sticky='nsew', padx=2, pady=2)

        for f_i in range(5):
            f_self.buttons_frame.columnconfigure(f_i, weight=1)
            f_self.buttons_frame.rowconfigure(f_i, weight=1)

        f_self.display = tk.Entry(f_self.main_window, justify='right')
        f_self.display.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

    def f_button_clicked(f_self, f_value):
        if f_value in '0123456789':
            f_self.f_append_display(f_value)
        elif f_value == 'C':
            f_self.f_clear_display()
        elif f_value in '+-*/':
            f_self.f_append_operator(f_value)
        elif f_value == '=':
            f_self.f_calculate_result()
        elif f_value == 'sqrt':
            f_self.f_calculate_square_root()

    def f_append_display(f_self, f_value):
        f_self.display.insert(tk.END, f_value)

    def f_clear_display(f_self):
        f_self.display.delete(0, tk.END)

    def f_append_operator(f_self, f_operator):
        f_self.display.insert(tk.END, f_operator)

    def f_calculate_result(f_self):
        f_expression = f_self.display.get()
        try:
            f_result = eval(f_expression, {'__builtins__': None}, {'Calculator': Calculator, 'calc': f_self.calc})
            f_self.f_clear_display()
            f_self.display.insert(tk.END, str(f_result))
        except Exception as f_error:
            f_self.f_clear_display()
            f_self.display.insert(tk.END, 'Error')

    def f_calculate_square_root(f_self):
        f_expression = f_self.display.get()
        try:
            f_alpha = float(f_expression)
            f_result = f_self.calc.f_square_root(f_alpha)
            f_self.f_clear_display()
            f_self.display.insert(tk.END, str(f_result))
        except Exception as f_error:
            f_self.f_clear_display()
            f_self.display.insert(tk.END, 'Error')

    def f_run(f_self):
        f_self.main_window.mainloop()


if __name__ == '__main__':
    f_gui_calc = f_GUI_Calculator()
    f_gui_calc.f_run()
