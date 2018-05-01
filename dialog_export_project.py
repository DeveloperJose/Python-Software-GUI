import Tkinter as tk
class ProjectExport(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("Project Export")

        label_1 = tk.Label(self, text="Export a project to the local file system")
        label_2 = tk.Label(self, text="Project")
        label_3 = tk.Label(self, text="To export file")
        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self)
        button1 = tk.Button(self, text="Browse", command=lambda: self.browse_dir(entry_1))
        button2 = tk.Button(self, text="Browse", command=lambda: self.open_location(entry_2))
        button3 = tk.Button(self, text="Export")
        button4 = tk.Button(self, text="Cancel", command=self.destroy)

        label_1.grid(row=0, columnspan=3)
        label_2.grid(row=1, sticky='E')
        label_3.grid(row=2, sticky='E')
        entry_1.grid(row=1, column=1)
        entry_2.grid(row=2, column=1)
        button1.grid(row=1, column=2)
        button2.grid(row=2, column=2)
        button3.grid(row=3, column=1, sticky='E')
        button4.grid(row=3, column=2)

    def browse_dir(self, e):
        directory = tk.tkFileDialog.askdirectory()
        dir = directory
        e.delete(0, tk.END)
        e.insert(0, dir)

    def open_location(self, e):
        filename = tk.tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("all files", ".*"), ("all files", "*.*")))
        e.delete(0, tk.END)
        e.insert(0, filename)