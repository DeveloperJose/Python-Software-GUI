import Tkinter as tk

class TitleBar(tk.Frame):
    def __init__(self, master, title):
        tk.Frame.__init__(self, master)

        self.title = tk.StringVar()
        self.title.set(title)
        self.lbl_title = tk.Label(self, text=title, textvariable=self.title, anchor='center', background="gray")

        self.close_img = tk.PhotoImage(file="close.gif").subsample(9, 9)
        self.close = tk.Button(self, image=self.close_img, command=self.on_close)

        self.min_img = tk.PhotoImage(file="minimize.gif").subsample(9,9)
        self.minimize = tk.Button(self, image=self.min_img, command=self.on_minimize)

        self.max_img = tk.PhotoImage(file="maximize.gif").subsample(9, 9)
        self.maximize = tk.Button(self, image=self.max_img, command=self.on_maximize)

        self.close.pack(side='right')
        self.maximize.pack(side='right')
        self.minimize.pack(side='right')
        self.lbl_title.pack(side='left', fill="x", expand=True)


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