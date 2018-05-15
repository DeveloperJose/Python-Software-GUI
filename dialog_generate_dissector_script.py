import Tkinter as tk
import tkFileDialog
from workspace import Workspace
class DialogGenerateDissectorScript(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("Dissector Script")

        self.lbl_gen = tk.Label(self, text="Generate a custom dissector script")
        self.lbl_project = tk.Label(self, text="Project")
        self.lbl_format = tk.Label(self, text="Dissector Format")
        self.lbl_save_location = tk.Label(self, text="Save Location")

        options = [p for p in Workspace.current.projects]
        self.var_option = tk.StringVar(self, options[Workspace.current.selected_project])
        self.var_format = tk.StringVar(self, "LUA")
        self.var_save_location = tk.StringVar(self)

        self.menu_project = tk.OptionMenu(self, self.var_option, *options)
        self.entry_format = tk.Entry(self, textvariable=self.var_format, state='disabled')
        self.entry_save = tk.Entry(self, textvariable=self.var_save_location)

        self.btn_browse = tk.Button(self, text="Browse", command=self.save_location)
        self.btn_generate = tk.Button(self, text="Generate", command=self.generate, state='disabled')
        self.btn_cancel = tk.Button(self, text="Cancel", command=self.destroy)

        self.lbl_gen.grid(row=0, columnspan=3)
        self.lbl_project.grid(row=1, sticky='E')
        self.lbl_format.grid(row=2, sticky='E')
        self.lbl_save_location.grid(row=3, sticky='E')

        self.menu_project.grid(row=1, column=1)
        self.entry_format.grid(row=2, column=1)
        self.entry_save.grid(row=3, column=1)
        self.btn_browse.grid(row=3, column=2)
        self.btn_generate.grid(row=4, column=1, sticky='E')
        self.btn_cancel.grid(row=4, column=2)

    def generate(self):
        pdt = Workspace.current.get_tree().to_xml()
        path = self.var_save_location.get()

        xmlfile = open(path, 'w')
        xmlfile.write(pdt)
        self.destroy()

    def save_location(self):
        filename = tkFileDialog.asksaveasfilename(initialdir="/", title="Select file",
                                                  filetypes=(("all files", ".*"), ("all files", "*.*")))
        self.var_save_location.set(filename)
        self.btn_generate['state'] = 'normal'