import Tkinter as tk

from titlebar import TitleBar

class TextWindow(tk.Frame):
    def __init__(self, title, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.title_bar = TitleBar(title, self)
        self.title_bar.set_max(lambda: self.text.grid())
        self.title_bar.set_min(lambda: self.text.grid_remove())
        self.text = tk.Text(self,width=35,height=20)

        self.title_bar.grid(column=0,row=0)
        self.text.grid(column=0,row=1)

    def insert(self, text):
        self.text.insert('insert', text)
