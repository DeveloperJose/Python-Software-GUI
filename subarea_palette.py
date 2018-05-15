import Tkinter as tk
import Tkdnd
from PIL import Image, ImageTk
from titlebar import TitleBar
from workspace import Workspace
from palette_dnd import Draggable
from palette_info import ConnectorInfo, FieldInfo, StartFieldInfo, EndFieldInfo
class PaletteType:
    START_FIELD = 0
    FIELD = 1
    END_FIELD = 2
    CONNECTOR = 3

class SubAreaPalette(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.is_field_open = True
        self.is_construct_open = True

        self.init_images()
        self.init_frames()
        self.init_fields()
        self.init_constructs()

    def init_images(self):
        self.im_folder_closed = ImageTk.PhotoImage(
            Image.open('folder_closed.png').resize((16, 16), Image.ANTIALIAS))
        self.im_folder_open = ImageTk.PhotoImage(Image.open('folder_opened.png').resize((16, 16), Image.ANTIALIAS))
        self.im_circle = ImageTk.PhotoImage(
            Image.open('circular-shape-silhouette.png').resize((40, 40), Image.ANTIALIAS))
        self.im_arrow = ImageTk.PhotoImage(Image.open('arrow-pointing-to-right.png'))
        self.im_diamond = ImageTk.PhotoImage(Image.open('rhombus.png').resize((40, 40), Image.ANTIALIAS))

    def init_frames(self):
        self.title_bar = TitleBar(self, 'Palette')
        self.title_bar.grid(column=0, row=0, columnspan=10, sticky='NWWE')

        self.frame_fields = tk.Frame(self, bg='white')
        self.frame_constructs = tk.Frame(self, bg='white')
        self.frame_decision = tk.Frame(self.frame_constructs)
        self.frame_connector = tk.Frame(self.frame_constructs)
        self.frame_expression = tk.Frame(self.frame_constructs)

        # Field Icon
        self.icon_field = tk.Label(self, text='', image=self.im_folder_open)
        self.lbl_field = tk.Label(self, text='Field', font=('', '12'))
        self.lbl_field.bind('<Button-1>', self.on_btn_click_field)
        self.icon_field.bind('<Button-1>', self.on_btn_click_field)

        # Construct Icon
        self.icon_construct = tk.Label(self, text='', image=self.im_folder_open)
        self.lbl_construct = tk.Label(self, text='Construct', font=('', '12'))
        self.lbl_construct.bind('<Button-1>', self.on_btn_click_construct)
        self.icon_construct.bind('<Button-1>', self.on_btn_click_construct)

        # Field Icon -> Field Frame -> Construct Icon -> Construct Frame
        self.icon_field.grid(row=1, column=0, sticky='WE')
        self.lbl_field.grid(row=1, column=1, columnspan=5, sticky='WE')

        self.frame_fields.grid(row=2, column=1, sticky='WE')

        self.icon_construct.grid(row=3, column=0, sticky='WE')
        self.lbl_construct.grid(row=3, column=1, columnspan=5, sticky='WE')

        self.frame_constructs.grid(row=4, column=1, columnspan=10, sticky='WE')

        # Decision Frame -> Connector Frame -> Expression Frame
        self.frame_decision.grid(column=0, row=1, columnspan=4, sticky='E')
        self.frame_connector.grid(column=0, row=2, columnspan=2, sticky='E')
        self.frame_expression.grid(column=0, row=3, columnspan=2, sticky='E')

    def init_fields(self):
        self.circlepic = tk.PhotoImage(file="circle.gif")
        self.sized_circle = self.circlepic.subsample(10, 10)
        self.circlebpic = tk.PhotoImage(file="circleb.gif")
        self.sized_circleb = self.circlebpic.subsample(10, 10)

        self.start_field = tk.Button(self.frame_fields,text='Start Field',image=self.sized_circle, compound='center')
        self.start_field.bind('<ButtonPress>',lambda event: self.on_dnd_start(event, PaletteType.START_FIELD))
        self.start_field.grid(column=0,row=1)

        self.field_1 = tk.Button(self.frame_fields, text='Field (1 byte)')
        self.field_1.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, PaletteType.FIELD))
        self.field_1.grid(column=1, row=1)

        self.field_2 = tk.Button(self.frame_fields, text='Field (2 byte')
        self.field_2.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, PaletteType.FIELD))
        self.field_2.grid(column=0, row=2)

        self.field_4 = tk.Button(self.frame_fields, text='Field (4 byte')
        self.field_4.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, PaletteType.FIELD))
        self.field_4.grid(column=1, row=2)

        self.field_8 = tk.Button(self.frame_fields, text='Field (8 byte')
        self.field_8.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, PaletteType.FIELD))
        self.field_8.grid(column=0, row=3)

        self.field_16 = tk.Button(self.frame_fields, text='Field (16 byte')
        self.field_16.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, PaletteType.FIELD))
        self.field_16.grid(column=0, row=3)

        self.end_field = tk.Button(self.frame_fields, text='End Field', image=self.sized_circleb, compound='center', fg='red')
        self.end_field.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, PaletteType.END_FIELD))
        self.end_field.grid(column=1, row=3)

    def init_constructs(self):
        self.init_decision_constructs()
        self.init_connector_constructs()
        self.init_expression_constructs()

    def init_decision_constructs(self):
        lbl_decision = tk.Label(self.frame_decision, text='Decision')
        lbl_decision.grid(column=0, row=0, sticky='W')

        btn_expression = tk.Button(self.frame_decision, text='Expression', image=self.im_diamond,
                                    compound=tk.CENTER)
        btn_expression.grid(column=0, row=1)

    def init_connector_constructs(self):
        lbl = tk.Label(self.frame_connector, text='Connector')
        lbl.grid(column=0, row=0, sticky='WE')

        connector = tk.Button(self.frame_connector, text='', image=self.im_arrow, compound=tk.CENTER, bg='white')
        connector.bind("<Button-1>", lambda event: self.on_dnd_start(event, PaletteType.CONNECTOR))
        connector.grid(column=0, row=1, sticky='WE')

    def init_expression_constructs(self):
        lbl = tk.Label(self.frame_expression, text='Expression')

        lbl2 = tk.Label(self.frame_expression, text='Relational Operator', bg='gray')
        op_frame1 = tk.Frame(self.frame_expression)
        op_less_than = tk.Button(op_frame1, text='<')
        op_less_than_equal = tk.Button(op_frame1, text='<=')
        op_greater_than = tk.Button(op_frame1, text='>')
        op_greater_than = tk.Button(op_frame1, text='>=')
        op_equal = tk.Button(op_frame1, text='==')
        op_not_equal = tk.Button(op_frame1, text='~=')

        lbl3 = tk.Label(self.frame_expression, text='Logical Operator')
        op_frame2 = tk.Frame(self.frame_expression)
        op_and = tk.Button(op_frame2, text='And')
        op_or = tk.Button(op_frame2, text='Or')
        op_not = tk.Button(op_frame2, text='Not')

        operand = tk.Button(self.frame_expression, text='Operand')

        lbl.grid(column=0, row=0, sticky='WE')
        lbl2.grid(column=0, row=1, sticky='WE')
        op_frame1.grid(column=0, row=2, sticky='WE')
        lbl3.grid(column=0, row=3, sticky='WE')
        op_frame2.grid(column=0, row=4)

        op_less_than.grid(column=1, row=0, sticky='WE')
        op_less_than_equal.grid(column=2, row=0, sticky='WE')
        op_greater_than.grid(column=3, row=0, sticky='WE')
        op_greater_than.grid(column=4, row=0, sticky='WE')
        op_equal.grid(column=5, row=0, sticky='WE')
        op_not_equal.grid(column=6, row=0, sticky='WE')

        op_and.grid(column=1, row=0, sticky='WE')
        op_or.grid(column=2, row=0, sticky='WE')
        op_not.grid(column=3, row=0, sticky='WE')

        operand.grid(column=0, row=7, sticky='WE')

    def on_btn_click_construct(self, event):
        if self.is_construct_open:
            self.icon_construct.configure(image=self.im_folder_closed)
            self.frame_constructs.grid_remove()
        else:
            self.icon_construct.configure(image=self.im_folder_open)
            self.frame_constructs.grid()

        self.is_construct_open = not self.is_construct_open

    def on_btn_click_field(self, event):
        if self.is_field_open:
            self.icon_field.configure(image=self.im_folder_closed)
            self.frame_fields.grid_remove()
        else:
            self.icon_field.configure(image=self.im_folder_open)
            self.frame_fields.grid()

        self.is_field_open = not self.is_field_open

    def on_dnd_start(self, event, type):
        # Create placeholder info and add it to tree
        print("dnd entered")
        ID = len(Workspace.current.get_tree().fields)
        info = self.info_from_type(ID, type)

        Workspace.current.get_tree().fields.insert(ID, info)

        ThingToDrag = Draggable(self, ID)
        Tkdnd.dnd_start(ThingToDrag, event)

    def info_from_type(self, ID, type):
        if type == PaletteType.START_FIELD:
            return StartFieldInfo()
        elif type == PaletteType.FIELD:
            return FieldInfo()
        elif type == PaletteType.END_FIELD:
            return EndFieldInfo()
        elif type == PaletteType.CONNECTOR:
            return ConnectorInfo()

        return StartFieldInfo()
