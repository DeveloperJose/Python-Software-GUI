class TitleBar(tk.Frame):
    def __init__(self, title, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.titles = tk.Label(self, text=title, anchor='center', background="gray")

        img = tk.PhotoImage(file="close.gif")
        self.close_img = img.subsample(9, 9)
        self.close = tk.Button(self, image=self.close_img, command=self.on_close)

        img = tk.PhotoImage(file="minimize.gif")
        self.min_img = img.subsample(9, 9)
        self.minimize = tk.Button(self, image=self.min_img, command=self.on_minimize)

        img = tk.PhotoImage(file="maximize.gif")
        self.max_img = img.subsample(9, 9)
        self.maximize = tk.Button(self, image=self.max_img, command=self.on_maximize)

        self.close.pack(side='right')
        self.maximize.pack(side='right')
        self.minimize.pack(side='right')

        self.titles.pack(side='left', fill="x", expand=True)

    def set_min(self, lamb):
        self.lamb1 = lamb

    def set_max(self, lamb):
        self.lamb2 = lamb

    def on_close(self):
        self.master.grid_remove()

    def on_minimize(self):
       try:
           self.lamb1()
       except:
           pass

    def on_maximize(self):
        try:
            self.lamb2()
        except:
            pass