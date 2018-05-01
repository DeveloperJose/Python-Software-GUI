class DBuilder(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # self.parent = parent
        # self.title('Dissector Builder Area')

        self.title_bar = TitleBar('Dissector Builder Area', self)
        self.title_bar.grid(column=0,row=0, columnspan=5, padx=1, pady=2, sticky='WE')

        self.frame_canvas = tk.Frame(self, bg='white')
        canvas = CanvasDnd(self.frame_canvas, bg='white', width=800, height=500)
        canvas.grid(column=0, row=1)
        tk.Label(self.frame_canvas, text='Canvas').grid(column=0, row=0, padx=2, pady=2)

        self.frame_palette = Palette(self)
        # self.frame_palette = tk.Frame(self, bg='red')
        # tk.Label(self.frame_palette, text='Palette').grid(column=0, row=0, columnspan=2)
        #
        # self.im = ImageTk.PhotoImage(Image.open('circular-shape-silhouette.png'))
        # lbl_field = tk.Label(self.frame_palette, text='Field', fg='white', image=self.im, compound=tk.CENTER)
        # lbl_field.grid(column=0, row=1)
        # lbl_field.bind('<ButtonPress>', self.on_dnd_start)

        # Layout
        self.frame_canvas.grid(column=0, row=1, sticky='WENS', padx=2, pady=2)
        self.frame_palette.grid(column=1, row=1, sticky='WENS', padx=2, pady=2)