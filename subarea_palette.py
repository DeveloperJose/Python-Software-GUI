import Tkdnd
import Tkinter as tk

from palette_dnd import Draggable
from palette_info import StartFieldInfo, ConnectorInfo, FieldInfo
from titlebar import TitleBar
from workspace import Workspace
class PaletteType:
    START_FIELD = 0
    CONNECTOR = 1
    FIELD = 2

class SubAreaPalette(tk.Frame):
    def on_dnd_start(self, event, type):
        # Create placeholder info and add it to tree
        ID = len(Workspace.current.get_tree().fields)
        info = self.info_from_type(ID, type)

        Workspace.current.get_tree().fields.insert(ID, info)

        ThingToDrag = Draggable(self, ID)
        Tkdnd.dnd_start(ThingToDrag, event)

    def info_from_type(self, ID, type):
        if type == PaletteType.START_FIELD:
            return StartFieldInfo()
        elif type == PaletteType.CONNECTOR:
            return ConnectorInfo()
        elif type == PaletteType.FIELD:
            return FieldInfo()
        return StartFieldInfo()

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.title_bar = TitleBar(self, 'Palette')
        self.title_bar.grid(column=0, row=0, columnspan=10, sticky='NWWE')

        self.btn_start_field = tk.Button(self, text='Start Field')
        self.btn_start_field.grid()
        self.btn_start_field.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, PaletteType.START_FIELD))

        self.btn_connector = tk.Button(self, text='Connector')
        self.btn_connector.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, PaletteType.CONNECTOR))
        self.btn_connector.grid()

        self.btn_field = tk.Button(self, text='Field')
        self.btn_field.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, PaletteType.FIELD))
        self.btn_field.grid()