import Tkinter as tk
from project import Project
class DialogNewProject(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("New Project")

        lbl_create = tk.Label(self, text="Create a new project")
        lbl_name = tk.Label(self, text="Project Name")
        lbl_desc = tk.Label(self, text="Description")

        btn_create = tk.Button(self, text="Create",command=self.show_entry_fields)
        btn_cancel = tk.Button(self, text="Cancel", command=self.destroy)

        self.entry_name = tk.Entry(self)
        self.entry_desc = tk.Entry(self)

        lbl_create.grid(row=0, column=1)
        lbl_name.grid(row=1, sticky='E')
        lbl_desc.grid(row=2, sticky='E')
        self.entry_name.grid(row=1, column=1)
        self.entry_desc.grid(row=2, column=1)
        btn_create.grid(row=3, column=1, sticky='E')
        btn_cancel.grid(row=3, column=2)

    def show_entry_fields(self):
        # print("Name of Project: %s\n Description: %s" % (self.entry_name.get(), self.entry_desc.get()))
        p = Project(self.entry_name.get(), self.entry_desc.get())
