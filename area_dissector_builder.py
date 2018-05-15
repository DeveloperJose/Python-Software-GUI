import Tkinter as tk

from dnd import CanvasDnd
from subarea_palette import SubAreaPalette
from titlebar import TitleBar

class AreaDissectorBuilder(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.title_bar = TitleBar(self, 'Dissector Builder Area')
        self.frame_canvas = tk.Frame(self, bg='white')
        self.frame_palette = SubAreaPalette(self)
        self.hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.vbar = tk.Scrollbar(self, orient=tk.VERTICAL)

        canvas = CanvasDnd(self.frame_canvas, bg='white', width=800, height=500, scrollregion=(0,0,5000,5000))
        canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.hbar.config(command=canvas.xview)
        self.vbar.config(command=canvas.yview)
        canvas.hbar = self.hbar
        canvas.vbar = self.vbar

        # lbl_canvas = tk.Label(self.frame_canvas, text='Canvas')

        # Parent set-up
        self.title_bar.pack(fill=tk.X, expand=True, side=tk.TOP)
        self.frame_palette.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)
        self.vbar.pack(fill=tk.Y, expand=False, side=tk.RIGHT)
        self.frame_canvas.pack(fill=tk.BOTH, expand=False)
        self.hbar.pack(fill=tk.X, expand=True)


        # Frame Canvas set-up
        canvas.pack(fill=tk.BOTH, expand=True)
