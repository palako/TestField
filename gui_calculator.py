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
            '0', 'C', '/', '='
        ]

        f_self.buttons = {}
        for f_index, f_text in enumerate(f_self.button_texts):
            f_command = lambda f_text=f_text: f_self.f_button_clicked(f_text)
            f_self.buttons[f_text] = tk.Button(f_self.buttons_frame, text=f_text, command=f_command)
            f_row, f_col = divmod(f_index, 4)
            f_self.buttons[f_text].grid(row=f_row, column=f_col, sticky='nsew', padx=2, pady=2)

        for f_i in range(4):
            f_self.buttons_frame.columnconfigure(f_i, weight=1)
            f_self.buttons_frame.rowconfigure(f_i, weight=1)

        f_self.display = tk.Entry(f_self.main_window, justify='right')
        f_self.display.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

    def f_button_clicked(f_self, f_value):
        print(f_value)  # Placeholder for button click handling

    def f_run(f_self):
        f_self.main_window.mainloop()

if __name__ == '__main__':
    f_gui_calc = f_GUI_Calculator()
    f_gui_calc.f_run()
