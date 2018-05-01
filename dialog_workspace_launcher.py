import Tkinter as tk
class WorkspaceLauncher(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("Workspace Launcher")

        dir = "C:"
        entry_1 = tk.Entry(self)
        entry_1.delete(0, tk.END)  # delete current text in entry
        entry_1.insert(0, dir)  # insert
        label_1 = tk.Label(self, text="Select a directory as workspace")
        label_2 = tk.Label(self, text="Workspace")
        button1 = tk.Button(self, text="Browse", command=lambda: self.browse_dir(entry_1))
        button2 = tk.Button(self, text="Launch")
        button3 = tk.Button(self, text="Cancel", command=self.destroy)

        label_1.grid(row=0, column=1)
        label_2.grid(row=1)
        entry_1.grid(row=1, column=1)
        button1.grid(row=1, column=2)
        button2.grid(row=2, column=1)
        button3.grid(row=2, column=2)

    def browse_dir(self, e):
        directory = tk.tkFileDialog.askdirectory()
        dir = directory
        e.delete(0, tk.END)
        e.insert(0, dir)