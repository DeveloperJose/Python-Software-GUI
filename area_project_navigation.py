import Tkinter as tk

from titlebar import TitleBar
from workspace import Workspace
class AreaProjectNavigation(tk.Frame):
    def on_click(self, var_name, lbl):
        # Close the previous project
        prev_lbl = self.lbls[Workspace.current.selected_project]
        prev_lbl['image'] = self.im_close

        # Open the new project
        lbl['image'] = self.im_open
        # idx = next((i for i in range(len(Workspace.current.projects)) if Workspace.current.projects[i] == var_name.get()), 0)
        # Workspace.current.selected_project = idx


    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.title_bar = TitleBar(self, 'Project Navigator')

        self.title_bar.bind()
        self.title_bar.pack(padx=2)

        self.label = tk.Label(self,text=Workspace.current.name)
        self.label.bind()
        self.label.pack()

        self.im_close = tk.PhotoImage(file="Closef.gif").subsample(5, 5)
        self.im_open = tk.PhotoImage(file="Openf.gif").subsample(5, 5)
        self.vars = []
        self.lbls = []

        for p in Workspace.current.projects:
            var_name = tk.StringVar(self, p.name)
            lbl = tk.Label(self, textvariable=var_name, compound='left', pady=10, padx=10, image=self.im_close)
            lbl.bind("<Button-1>", lambda event: self.on_click(var_name, lbl))
            lbl.pack()

            self.vars.append(var_name)
            self.lbls.append(lbl)

        self.lbls[Workspace.current.selected_project]['image'] = self.im_open