import Tkinter as tk
import Tkdnd
from PIL import Image, ImageTk
from titlebar import TitleBar
from window_type import WindowType

from palette_field import FieldDialog
from palette_start_field import StartField
from palette_end_field import EndField
from palette_packet_information import PacketInformationField
from palette_reference_list import ReferenceListField

from drag_button import DragButton

from palette_draggable import PaletteDraggable, StartFieldView, Tree, StartFieldInfo

class PaletteType:
    START_FIELD = 0

class Palette(tk.Frame):

    def on_dnd_start(self, event, type):
        # Create placeholder info and add it to tree
        ID = len(Tree.current.fields)
        info = self.info_from_type(ID, type)

        Tree.current.fields.insert(ID, info)

        ThingToDrag = PaletteDraggable(self, ID)
        Tkdnd.dnd_start(ThingToDrag, event)

    def info_from_type(self, ID, type):
        if type == PaletteType.START_FIELD:
            return StartFieldInfo()
        return StartFieldInfo()

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.title_bar = TitleBar('Palette', self)
        self.title_bar.grid(column=0, row=0, columnspan=10, sticky='NWWE')

        Tree.current = Tree()

        self.btn = tk.Button(self, text='Start Field')
        self.btn.grid()
        self.btn.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, PaletteType.START_FIELD))