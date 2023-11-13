import tkinter as tk
from calculator import Calculator

class f_GUI_Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('Calculator')
        self.calc = Calculator()
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.master)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.buttons = {
            'add': tk.Button(self.master, text='+', command=lambda: self.f_press_operation('f_add')),
            'subtract': tk.Button(self.master, text='-', command=lambda: self.f_press_operation('f_subtract')),
            'multiply': tk.Button(self.master, text='*', command=lambda: self.f_press_operation('f_multiply')),
            'divide': tk.Button(self.master, text='/', command=lambda: self.f_press_operation('f_divide')),
            'square_root': tk.Button(self.master, text='√', command=lambda: self.f_press_operation('f_square_root')),
            'equals': tk.Button(self.master, text='=', command=self.f_calculate_result),
            'clear': tk.Button(self.master, text='C', command=self.f_clear_entry)
        }

        self.buttons['add'].grid(row=1, column=0)
        self.buttons['subtract'].grid(row=1, column=1)
        self.buttons['multiply'].grid(row=1, column=2)
        self.buttons['divide'].grid(row=1, column=3)
        self.buttons['square_root'].grid(row=2, column=0)
        self.buttons['equals'].grid(row=2, column=1)
        self.buttons['clear'].grid(row=2, column=2)

    def f_press_operation(self, operation):
        self.current_operation = operation
        self.alpha = float(self.entry.get())
        self.entry.delete(0, tk.END)

    def f_calculate_result(self):
        self.beta = float(self.entry.get())
        result = getattr(self.calc, self.current_operation)(self.alpha, self.beta)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(result))

    def f_clear_entry(self):
        self.entry.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = f_GUI_Calculator(root)
    root.mainloop()
