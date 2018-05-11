import Tkinter as tk
class Table(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent
        self.components = {}
        self.column = 0
        self.row = 0

        # self.configure(background='black')

    def __add__(self, name, component):
        lbl = tk.Label(self, text=name, borderwidth=0)
        self.components[name] = component

        lbl.grid(column=0, row=self.row)
        component.grid(column=1, row=self.row)
        self.row += 1

    def add_entry(self, name, command=None, state='normal', width=65):
        entry = tk.Entry(self, validate='focusout', validatecommand=command, state=state)
        entry.config(width=width)
        self.__add__(name, entry)

    def add_labels(self, text1, text2):
        lbl = tk.Label(self, text=text2)
        self.__add__(text1, lbl)

    def add_option(self, name, options, default, command=None, state='normal', width=58):
        var = tk.StringVar()
        var.set(default)
        option = tk.OptionMenu(self, var, *options, command=command)
        option.config(state=state, width=width)
        self.__add__(name, option)

    def add_checkbox(self, name, command=None, state='normal'):
        checkbox = tk.Checkbutton(self, state=state, command=command)
        self.__add__(name, checkbox)
