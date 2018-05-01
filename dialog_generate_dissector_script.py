import Tkinter as tk
class DissectorScript(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("Dissector Script")

        label_1 = tk.Label(self, text="Generate a custom dissector script")
        label_2 = tk.Label(self, text="Project")
        label_3 = tk.Label(self, text="Dissector Format")
        label_4 = tk.Label(self, text="Save Location")
        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self)
        entry_3 = tk.Entry(self)
        button1 = tk.Button(self, text="Browse", command=lambda: self.open_location(entry_1))
        button2 = tk.Button(self, text="Browse", command=lambda: self.save_location(entry_3))
        button3 = tk.Button(self, text="Generate")
        button4 = tk.Button(self, text="Cancel", command=self.destroy)

        label_1.grid(row=0, columnspan=3)
        label_2.grid(row=1, sticky='E')
        label_3.grid(row=2, sticky='E')
        label_4.grid(row=3, sticky='E')
        entry_1.grid(row=1, column=1)
        entry_2.grid(row=2, column=1)
        entry_3.grid(row=3, column=1)
        button1.grid(row=1, column=2)
        button2.grid(row=3, column=2)
        button3.grid(row=4, column=1, sticky='E')
        button4.grid(row=4, column=2)

    def save_location(self, e):
        filename = tk.tkFileDialog.asksaveasfilename(initialdir="/", title="Select file",
                                                  filetypes=(("all files", ".*"), ("all files", "*.*")))
        e.delete(0, tk.END)
        e.insert(0, filename)

    def open_location(self, e):
        filename = tk.tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("all files", ".*"), ("all files", "*.*")))
        e.delete(0, tk.END)
        e.insert(0, filename)