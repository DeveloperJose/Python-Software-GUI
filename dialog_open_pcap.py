import Tkinter as tk
class PCAP(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("PCAP")

        entry_1 = tk.Entry(self)
        label_1 = tk.Label(self, text="Open a PCAP file")
        label_2 = tk.Label(self, text="PCAP Name")
        button1 = tk.Button(self, text="Browse", command=lambda: self.open_location(entry_1))
        button2 = tk.Button(self, text="Open")
        button3 = tk.Button(self, text="Cancel", command=self.destroy)

        label_1.grid(row=0, columnspan=3)
        label_2.grid(row=1)
        entry_1.grid(row=1, column=1)
        button1.grid(row=1, column=2)
        button2.grid(row=2, column=1)
        button3.grid(row=2, column=2)

    def open_location(self, e):
        filename = tk.tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("all files", ".*"), ("all files", "*.*")))
        e.delete(0, tk.END)
        e.insert(0, filename)