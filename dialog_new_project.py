import Tkinter as tk
class NewProject(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("New Project")

        label_1 = tk.Label(self, text="Create a new project")
        label_2 = tk.Label(self, text="Project Name")
        label_3 = tk.Label(self, text="Description")
        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self)
        button1 = tk.Button(self, text="Create")
        button2 = tk.Button(self, text="Cancel", command=self.destroy)

        label_1.grid(row=0, column=1)
        label_2.grid(row=1, sticky='E')
        label_3.grid(row=2, sticky='E')
        entry_1.grid(row=1, column=1)
        entry_2.grid(row=2, column=1)
        button1.grid(row=3, column=1, sticky='E')
        button2.grid(row=3, column=2)