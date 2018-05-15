import Tkinter as tk

from area_console import AreaConsole
from area_dissected_stream import AreaDissectedStream
from area_dissector_builder import AreaDissectorBuilder
from area_packet_stream import AreaPacketStream
from area_project_navigation import AreaProjectNavigation
from area_raw_data import AreaRawData
from dialog_export_project import DialogExportProject
from dialog_generate_dissector_script import DialogGenerateDissectorScript
from dialog_import_project import DialogImportProject
from dialog_new_project import DialogNewProject
from dialog_open_pcap import DialogOpenPCAP
from dialog_organize_views import DialogOrganizeViews
from dialog_workspace_launcher import DialogWorkspaceLauncher

class WindowType():
    WINDOW_FIELD = 0
    WINDOW_START_FIELD = 1
    WINDOW_END_FIELD = 2
    WINDOW_RLIST = 3
    WINDOW_PINFO = 4
    WINDOW_WORKSPACE_LAUNCHER=5
    WINDOW_NEW_PROJECT=6
    WINDOW_DISSECTOR_SCRIPT=7
    WINDOW_PROJECT_IMPORT=8
    WINDOW_PROJECT_EXPORT=9
    WINDOW_ORGANIZE_VIEWS=10
    WINDOW_OPEN_PCAP=11

class AreaWorkspace(tk.Tk):
    def new_window(self, type):
        if type == WindowType.WINDOW_WORKSPACE_LAUNCHER:
            form = DialogWorkspaceLauncher(None)
        elif type == WindowType.WINDOW_NEW_PROJECT:
            form = DialogNewProject(None)
        elif type == WindowType.WINDOW_DISSECTOR_SCRIPT:
            form = DialogGenerateDissectorScript(None)
        elif type == WindowType.WINDOW_PROJECT_IMPORT:
            form = DialogImportProject(None)
        elif type == WindowType.WINDOW_PROJECT_EXPORT:
            form = DialogExportProject(None)
        elif type == WindowType.WINDOW_ORGANIZE_VIEWS:
            form = DialogOrganizeViews(None)
        elif type == WindowType.WINDOW_OPEN_PCAP:
            form = DialogOpenPCAP(None)

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Protocol Dissector Generator System')

        import workspace
        workspace.Workspace.current = workspace.Workspace('Example')

        center = tk.Frame(self)
        top = tk.Frame(self)
        left = AreaProjectNavigation(self)
        center.grid(row=1,column=1, sticky='NEWS', padx=0, pady=2)
        top.grid(row=0,column=1, sticky='N', padx=2, pady=2)
        left.grid(row=1,column=0, sticky='NS', padx=1, pady=2)

        center_top = AreaDissectorBuilder(center)
        center_bottom = tk.Frame(center)
        psa = AreaPacketStream(center_bottom)
        dsa = AreaDissectedStream(center_bottom)
        rda = AreaRawData(center_bottom)
        ca = AreaConsole(center_bottom)

        center_top.grid(column=0,row=0, sticky="NS")
        center_bottom.grid(column=0, row=1, sticky='NS')
        psa.grid(column=0,row=0,sticky='E')
        dsa.grid(column=1,row=0,sticky='E')
        rda.grid(column=2,row=0,sticky='E')
        ca.grid(column=3,row=0,sticky='E')

        button_createProject = tk.Button(top, text='Create Project', command=lambda:self.new_window(WindowType.WINDOW_NEW_PROJECT))
        button_saveProject = tk.Button(top, text='Save Project')
        button_closeProject = tk.Button(top, text='Close Project', command=lambda:self.quit())
        button_switchWorkspace = tk.Button(top, text='Switch Workspace', command=lambda:self.new_window(WindowType.WINDOW_WORKSPACE_LAUNCHER))
        button_importProject = tk.Button(top, text='Import Project', command=lambda:self.new_window(WindowType.WINDOW_PROJECT_IMPORT))
        button_exportProject = tk.Button(top, text='Export Project', command=lambda:self.new_window(WindowType.WINDOW_PROJECT_EXPORT))
        button_generateDissectorS = tk.Button(top, text='Generate Dissector Script', command=lambda:self.new_window(WindowType.WINDOW_DISSECTOR_SCRIPT))
        button_organizeViews = tk.Button(top, text='Organize Views', command=lambda:self.new_window(WindowType.WINDOW_ORGANIZE_VIEWS))
        button_openPCAP = tk.Button(top, text='Open PCAP', command=lambda:self.new_window(WindowType.WINDOW_OPEN_PCAP))

        # place the buttons in the top frame
        button_createProject.grid(row=0, column=0, padx=5, pady=2)
        button_saveProject.grid(row=0, column=1, padx=5, pady=2)
        button_closeProject.grid(row=0, column=2, padx=5, pady=2)
        button_switchWorkspace.grid(row=0, column=3, padx=5, pady=2)
        button_importProject.grid(row=0, column=4, padx=5, pady=2)
        button_exportProject.grid(row=0, column=5, padx=5, pady=2)
        button_generateDissectorS.grid(row=0, column=6, padx=5, pady=2)
        button_organizeViews.grid(row=0, column=7, padx=5, pady=2)
        button_openPCAP.grid(row=0, column=8, padx=5, pady=2)