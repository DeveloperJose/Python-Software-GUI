import Tkinter as tk


class ProjectImport(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("Project Import")

        label_1 = tk.Label(self, text="Import a project into the current workspace")
        label_2 = tk.Label(self, text="Project")
        entry_1 = tk.Entry(self)
        button1 = tk.Button(self, text="Browse", command=lambda: self.browse_dir(entry_1))
        button2 = tk.Button(self, text="Import")
        button3 = tk.Button(self, text="Cancel", command=self.destroy)

        label_1.grid(row=0, columnspan=3)
        label_2.grid(row=1, sticky='E')
        entry_1.grid(row=1, column=1)
        button1.grid(row=1, column=2)
        button2.grid(row=2, column=1)
        button3.grid(row=2, column=2, sticky='E')

    def browse_dir(self, e):
        directory = tk.tkFileDialog.askdirectory()
        dir = directory
        e.delete(0, tk.END)
        e.insert(0, dir)