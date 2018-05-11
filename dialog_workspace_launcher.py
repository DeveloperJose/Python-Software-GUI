import Tkinter as tk, tkFileDialog
import os
from workspace import Workspace
from project import Project

class DialogWorkspaceLauncher(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("Workspace Launcher")

        self.entry_path = tk.Entry(self)
        self.entry_path.insert(0, 'C:/')  # Default

        self.lbl_select = tk.Label(self, text="Select a directory as workspace")
        self.lbl_workspace = tk.Label(self, text="Workspace")

        self.btn_browse = tk.Button(self, text="Browse", command=self.on_click_browse)
        self.btn_launch = tk.Button(self, text="Launch", command=self.on_click_launch)
        self.btn_cancel = tk.Button(self, text="Cancel", command=self.destroy)

        self.lbl_select.grid(row=0, column=1)
        self.lbl_workspace.grid(row=1)
        self.entry_path.grid(row=1, column=1)
        self.btn_browse.grid(row=1, column=2)
        self.btn_launch.grid(row=2, column=1)
        self.btn_cancel.grid(row=2, column=2)

    def on_click_launch(self):
        dir = self.entry_path.get()

        # Create workspace
        name = os.path.basename(dir)
        workspace = Workspace(name)

        # Read all the projects
        for filename in os.listdir(dir):
            if filename.endswith(".xml"):
                # Open XML and create a project
                xml = None
                p = Project.load_from_xml(xml)
                if p is not None:
                    workspace.projects.append(p)

        Workspace.current = workspace

        # import area_workspace
        # area_workspace.AreaWorkspace(None)
        # self.destroy()

    def on_click_browse(self):
        dir = tkFileDialog.askdirectory()
        self.entry_path.delete(0, tk.END)
        self.entry_path.insert(0, dir)