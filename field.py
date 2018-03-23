import Tkinter as tk
import Tkdnd
from dnd import Dragged, CanvasDnd
from PIL import Image, ImageTk

class Table(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent
        self.components = {}
        self.column = 0
        self.row = 0

        # self.configure(background='black')

    def __add__(self, name, component):
        lbl = tk.Label(self, text=name, borderwidth=0)
        self.components[name] = component

        lbl.grid(column=0, row=self.row)
        component.grid(column=1, row=self.row)
        self.row += 1

    def add_entry(self, name, command=None, state='normal', width=65):
        entry = tk.Entry(self, validate='focusout', validatecommand=command, state=state)
        entry.config(width=width)
        self.__add__(name, entry)

    def add_labels(self, text1, text2):
        lbl = tk.Label(self, text=text2)
        self.__add__(text1, lbl)

    def add_option(self, name, options, default, command=None, state='normal', width=58):
        var = tk.StringVar()
        var.set(default)
        option = tk.OptionMenu(self, var, *options, command=command)
        option.config(state=state, width=width)
        self.__add__(name, option)

    def add_checkbox(self, name, command=None, state='normal'):
        checkbox = tk.Checkbutton(self, state=state, command=command)
        self.__add__(name, checkbox)

class WorkspaceLauncher(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("Workspace Launcher")

        dir = "C:"
        entry_1 = tk.Entry(self)
        entry_1.delete(0, tk.END)  # delete current text in entry
        entry_1.insert(0, dir)  # insert
        label_1 = tk.Label(self, text="Select a directory as workspace")
        label_2 = tk.Label(self, text="Workspace")
        button1 = tk.Button(self, text="Browse", command=lambda: browse_dir(entry_1))
        button2 = tk.Button(self, text="Launch")
        button3 = tk.Button(self, text="Cancel", command=self.destroy)

        label_1.grid(row=0, column=1)
        label_2.grid(row=1)
        entry_1.grid(row=1, column=1)
        button1.grid(row=1, column=2)
        button2.grid(row=2, column=1)
        button3.grid(row=2, column=2)

class NewProject(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("New Project")

        label_1 = tk.Label(self, text="Create a new project")
        label_2 = tk.Label(self, text="Project Name")
        label_3 = tk.Label(self, text="Description")
        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self)
        button1 = tk.Button(self, text="Create")
        button2 = tk.Button(self, text="Cancel", command=self.destroy)

        label_1.grid(row=0, column=1)
        label_2.grid(row=1, sticky='E')
        label_3.grid(row=2, sticky='E')
        entry_1.grid(row=1, column=1)
        entry_2.grid(row=2, column=1)
        button1.grid(row=3, column=1, sticky='E')
        button2.grid(row=3, column=2)

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
        button1 = tk.Button(self, text="Browse", command=lambda: open_location(entry_1))
        button2 = tk.Button(self, text="Browse", command=lambda: save_location(entry_3))
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

class ProjectImport(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("Project Import")

        label_1 = tk.Label(self, text="Import a project into the current workspace")
        label_2 = tk.Label(self, text="Project")
        entry_1 = tk.Entry(self)
        button1 = tk.Button(self, text="Browse", command=lambda: browse_dir(entry_1))
        button2 = tk.Button(self, text="Import")
        button3 = tk.Button(self, text="Cancel", command=self.destroy)

        label_1.grid(row=0, columnspan=3)
        label_2.grid(row=1, sticky='E')
        entry_1.grid(row=1, column=1)
        button1.grid(row=1, column=2)
        button2.grid(row=2, column=1)
        button3.grid(row=2, column=2, sticky='E')

class ProjectExport(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("Project Export")

        label_1 = tk.Label(self, text="Export a project to the local file system")
        label_2 = tk.Label(self, text="Project")
        label_3 = tk.Label(self, text="To export file")
        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self)
        button1 = tk.Button(self, text="Browse", command=lambda: browse_dir(entry_1))
        button2 = tk.Button(self, text="Browse", command=lambda: open_location(entry_2))
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

class OrganizeViews(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("Organize Views")
        v_2 = tk.IntVar()
        v_3 = tk.IntVar()
        v_4 = tk.IntVar()
        v_5 = tk.IntVar()
        v_6 = tk.IntVar()
        v_7 = tk.IntVar()
        v_8 = tk.IntVar()

        label_1 = tk.Label(self, text="Customize the views")
        label_2 = tk.Label(self, text="Project Navigation")
        label_3 = tk.Label(self, text="Dissector Building Area")
        label_4 = tk.Label(self, text="Palette")
        label_5 = tk.Label(self, text="Packet Stream Area")
        label_6 = tk.Label(self, text="Dissected Stream Area")
        label_7 = tk.Label(self, text="Raw Data Area")
        label_8 = tk.Label(self, text="Console Area")
        label_9 = tk.Label(self, text="Hide")
        label_10 = tk.Label(self, text="Show")
        button1 = tk.Button(self, text="Restore to Default")
        button2 = tk.Button(self, text="Confirm", command=self.destroy)
        button3 = tk.Button(self, text="Cancel", command=self.destroy)
        radio_button_hide_2 = tk.Radiobutton(self, variable= v_2 , value=0)
        radio_button_hide_3 = tk.Radiobutton(self, variable= v_3 , value=0)
        radio_button_hide_4 = tk.Radiobutton(self, variable= v_4 , value=0)
        radio_button_hide_5 = tk.Radiobutton(self, variable= v_5 , value=0)
        radio_button_hide_6 = tk.Radiobutton(self, variable= v_6 , value=0)
        radio_button_hide_7 = tk.Radiobutton(self, variable= v_7 , value=0)
        radio_button_hide_8 = tk.Radiobutton(self, variable= v_8 , value=0)
        radio_button_show_2 = tk.Radiobutton(self, variable= v_2 , value=1)
        radio_button_show_3 = tk.Radiobutton(self, variable= v_3 , value=1)
        radio_button_show_4 = tk.Radiobutton(self, variable= v_4 , value=1)
        radio_button_show_5 = tk.Radiobutton(self, variable= v_5 , value=1)
        radio_button_show_6 = tk.Radiobutton(self, variable= v_6 , value=1)
        radio_button_show_7 = tk.Radiobutton(self, variable= v_7 , value=1)
        radio_button_show_8 = tk.Radiobutton(self, variable= v_8 , value=1)
        label_1.grid(row=0, columnspan=3)
        label_9.grid(row=1, column=1)
        label_10.grid(row=1, column=2)
        label_2.grid(row=2)
        label_3.grid(row=3)
        label_4.grid(row=4)
        label_5.grid(row=5)
        label_6.grid(row=6)
        label_7.grid(row=7)
        label_8.grid(row=8)
        radio_button_hide_2.grid(row=2, column=1)
        radio_button_hide_3.grid(row=3, column=1)
        radio_button_hide_4.grid(row=4, column=1)
        radio_button_hide_5.grid(row=5, column=1)
        radio_button_hide_6.grid(row=6, column=1)
        radio_button_hide_7.grid(row=7, column=1)
        radio_button_hide_8.grid(row=8, column=1)
        radio_button_show_2.grid(row=2, column=2)
        radio_button_show_3.grid(row=3, column=2)
        radio_button_show_4.grid(row=4, column=2)
        radio_button_show_5.grid(row=5, column=2)
        radio_button_show_6.grid(row=6, column=2)
        radio_button_show_7.grid(row=7, column=2)
        radio_button_show_8.grid(row=8, column=2)
        button1.grid(row=9, column=1)
        button2.grid(row=9, column=2)
        button3.grid(row=9, column=3)

class PCAP(tk.Toplevel):
    def __init__(self, *args, **kargs):
        tk.Toplevel.__init__(self, *args, **kargs)
        self.title("PCAP")

        entry_1 = tk.Entry(self)
        label_1 = tk.Label(self, text="Open a PCAP file")
        label_2 = tk.Label(self, text="PCAP Name")
        button1 = tk.Button(self, text="Browse", command=lambda: open_location(entry_1))
        button2 = tk.Button(self, text="Open")
        button3 = tk.Button(self, text="Cancel", command=self.destroy)

        label_1.grid(row=0, columnspan=3)
        label_2.grid(row=1)
        entry_1.grid(row=1, column=1)
        button1.grid(row=1, column=2)
        button2.grid(row=2, column=1)
        button3.grid(row=2, column=2)

class TitleBar(tk.Frame):
    def __init__(self, title, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.titles = tk.Label(self, text=title, anchor='center', background="gray")

        img = tk.PhotoImage(file="close.gif")
        self.close_img = img.subsample(9, 9)
        self.close = tk.Button(self, image=self.close_img, command=self.on_close)

        img = tk.PhotoImage(file="minimize.gif")
        self.min_img = img.subsample(9, 9)
        self.minimize = tk.Button(self, image=self.min_img, command=self.on_minimize)

        img = tk.PhotoImage(file="maximize.gif")
        self.max_img = img.subsample(9, 9)
        self.maximize = tk.Button(self, image=self.max_img, command=self.on_maximize)

        self.close.pack(side='right')
        self.maximize.pack(side='right')
        self.minimize.pack(side='right')

        self.titles.pack(side='left', fill="x", expand=True)

    def set_min(self, lamb):
        self.lamb1 = lamb

    def set_max(self, lamb):
        self.lamb2 = lamb

    def on_close(self):
        self.master.grid_remove()

    def on_minimize(self):
       try:
           self.lamb1()
       except:
           pass

    def on_maximize(self):
        try:
            self.lamb2()
        except:
            pass

import Tkinter, Tkconstants, tkFileDialog
def browse_dir(e):
    directory = tkFileDialog.askdirectory()
    dir = directory
    e.delete(0, tk.END)
    e.insert(0, dir)

def save_location(e):
    filename = tkFileDialog.asksaveasfilename(initialdir="/", title="Select file",
                                                   filetypes=(("all files", ".*"), ("all files", "*.*")))
    e.delete(0, tk.END)
    e.insert(0, filename)

def open_location(e):
    filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                 filetypes=(("all files", ".*"), ("all files", "*.*")))
    e.delete(0, tk.END)
    e.insert(0, filename)

class FieldDialog(Table):
    def __init__(self, parent):
        Table.__init__(self, parent)
        self.init_components()

    def init_components(self):
        self.set_title("Abbreviation")
        self.data_types = ['None','Protocol','Boolean','UInt8','UInt16','UInt24',
                           'UInt32','UInt64','Int8', 'Int16', 'Int24', 'Int32', 'Int64',
                           'Float', 'Double', 'Absolute_Time', 'Relative_Time', 'String',
                           'StringZ', 'UInt_String', 'Ether', 'Bytes', 'UInt_Bytes', 'IPv4',
                           'IPv6', 'IPxNet', 'FrameNum', 'PCRE', 'GUID', 'OID', 'EUI64'
                           ]
        self.bases = ['None', 'Dec', 'Hex', 'Oct', 'Dec_Hex', 'Hex_Dec']

        self.add_entry('Name')
        self.add_entry('Abbreviation', command=self.on_abbr_change)
        self.add_entry('Description')
        self.add_option('Reference List', options=['None'], default='Select from a predefined list of reference lists')
        self.add_option('Data Type', options=self.data_types, default='Select from a list of data types')
        self.add_option('Base', options=self.bases, default='Select from a list of bases')
        self.add_entry('Mask')
        self.add_entry('Value Constraint')
        self.add_checkbox('Required')

    def set_title(self, title):
        self.title("Field " + "[" + title + "]")

    def on_abbr_change(self):
        new_abbr = self.components['Abbreviation'].get()
        self.set_title(new_abbr)

class StartField(Table):
    def __init__(self, parent):
        Table.__init__(self, parent)

        self.set_title('Protocol Name')
        self.add_entry('Protocol Name', command=self.on_protocolname_change)
        self.add_entry('Protocol Description')
        self.add_entry('Dependent Protocol Name')
        self.add_entry('Dependency Pattern')

    def set_title(self, title):
        self.title("Start Field [" + title + "]")

    def on_protocolname_change(self):
        new_title = self.components['Protocol Name'].get()
        self.set_title(new_title)

class EndField(Table):
    def __init__(self, parent):
        Table.__init__(self, parent)

class ReferenceListField(Table):
    def __init__(self, parent):
        Table.__init__(self, parent)
        self.init_components()

        self.references = []
        self.add_reference_slot()

    def set_title(self, title):
        self.title("Reference List [" + title + "]")

    def init_components(self):
        self.set_title('Reference List Name')
        self.add_entry('Reference List Name', width=45, command=self.on_referencename_change)

        self.lbl_value = tk.Label(self, text='Value')
        self.lbl_desc = tk.Label(self, text='Text Description')
        self.lbl_value.grid(column=0, row=self.row)
        self.lbl_desc.grid(column=1, row=self.row)
        self.row += 1

        self.im = Image.open('plus-symbol-round-button.png')
        self.img_btn = ImageTk.PhotoImage(self.im)
        self.btn_add = tk.Button(self, image=self.img_btn, command=self.on_btn_add)
        self.lbl = {self.img_btn}

    def on_btn_add(self):
        (var_value, var_desc) = self.references[-1]
        if not var_value.get() or not var_desc.get():
            pass
        else:
            self.add_reference_slot()

    def on_referencename_change(self):
        new_title = self.components['Reference List Name'].get()
        self.set_title(new_title)

    def add_reference_slot(self):
        var_value = tk.StringVar()
        desc_value = tk.StringVar()
        self.references.append((var_value, desc_value))

        entry_value = tk.Entry(self, textvariable=var_value, width=15)
        entry_desc = tk.Entry(self, textvariable=desc_value, width=50)

        entry_value.grid(column=0, row=self.row)
        entry_desc.grid(column=1, row=self.row)
        self.row += 1

        self.btn_add.grid(column=1, row=self.row+1)

class PacketInformationField(Table):
    def __init__(self, parent):
        Table.__init__(self, parent)
        self.init_components()

        self.info = []
        self.add_info_slot()

    def init_components(self):
        self.title('Packet Information')
        self.lbl_value = tk.Label(self, text='Value')
        self.lbl_desc = tk.Label(self, text='Text Description')
        self.lbl_value.grid(column=0, row=self.row)
        self.lbl_desc.grid(column=1, row=self.row)
        self.row += 1

        self.im = Image.open('plus-symbol-round-button.png')
        self.img_btn = ImageTk.PhotoImage(self.im)
        self.btn_add = tk.Button(self, image=self.img_btn, command=self.on_btn_add)
        self.lbl = {self.img_btn}

        self.btn_add.grid(column=1, row=self.row + 1)

    def on_btn_add(self):
        (var_value, var_desc) = self.info[-1]
        if not var_value.get() or not var_desc.get():
            pass
        else:
            self.add_info_slot()

    def add_info_slot(self):
        var_value = tk.StringVar()
        desc_value = tk.StringVar()
        self.info.append((var_value, desc_value))

        entry_value = tk.Entry(self, textvariable=var_value)
        entry_desc = tk.Entry(self, textvariable=desc_value)

        entry_value.grid(column=0, row=self.row)
        entry_desc.grid(column=1, row=self.row)
        self.row += 1

        self.btn_add.grid(column=1, row=self.row+1)

class DragButton(tk.Button):
    def on_dnd_start(self, event, name, component):
        ThingToDrag = Dragged(name, component)
        Tkdnd.dnd_start(ThingToDrag, event)

    def __init__(self, parent, text, command=None, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.configure(text=text, command=command)
        self.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, text, self))

class TextWindow(tk.Frame):
    def __init__(self, title, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.title_bar = TitleBar(title, self)
        self.title_bar.set_max(lambda: self.text.grid())
        self.title_bar.set_min(lambda: self.text.grid_remove())
        self.text = tk.Text(self,width=35,height=20)

        self.title_bar.grid(column=0,row=0)
        self.text.grid(column=0,row=1)

    def insert(self, text):
        self.text.insert('insert', text)

class ConsoleArea(TextWindow):
    def __init__(self, *args, **kwargs):
        TextWindow.__init__(self, "Console", *args, **kwargs)


class PacketStreamArea(TextWindow):
    def __init__(self, *args, **kwargs):
        TextWindow.__init__(self, "Packet Stream Area", *args, **kwargs)


class RawDataArea(TextWindow):
    def __init__(self, *args, **kwargs):
        TextWindow.__init__(self, "Raw Data Area", *args, **kwargs)


class DissectedStreamArea(TextWindow):
    def __init__(self, *args, **kwargs):
        TextWindow.__init__(self, "Dissected Stream Area", *args, **kwargs)

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

class Palette(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.is_field_open = True
        self.is_construct_open = True

        self.init_images()
        self.init_frames()
        self.init_fields()
        self.init_constructs()

    def new_window(self, type):
        if type == WindowType.WINDOW_FIELD:
            form = FieldDialog(None)
        elif type == WindowType.WINDOW_START_FIELD:
            form = StartField(None)
        elif type == WindowType.WINDOW_END_FIELD:
            form = EndField(None)
        elif type == WindowType.WINDOW_RLIST:
            form = ReferenceListField(None)
        elif type == WindowType.WINDOW_PINFO:
            form = PacketInformationField(None)

        # top = tk.Toplevel(form)

        # root = tk.Tk()
        # root.withdraw()

    def init_images(self):
        self.im_folder_closed = ImageTk.PhotoImage(Image.open('folder_closed.png').resize((16,16), Image.ANTIALIAS))
        self.im_folder_open = ImageTk.PhotoImage(Image.open('folder_opened.png').resize((16,16), Image.ANTIALIAS))
        self.im_circle = ImageTk.PhotoImage(Image.open('circular-shape-silhouette.png').resize((40,40), Image.ANTIALIAS))
        self.im_arrow = ImageTk.PhotoImage(Image.open('arrow-pointing-to-right.png'))
        self.im_diamond = ImageTk.PhotoImage(Image.open('rhombus.png').resize((40,40), Image.ANTIALIAS))

    def init_frames(self):
        self.title_bar = TitleBar('Palette', self)
        self.title_bar.grid(column=0,row=0, columnspan=10,sticky='NWWE')

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
        self.icon_field.grid(row=1,column=0,sticky='WE')
        self.lbl_field.grid(row=1,column=1,columnspan=5,sticky='WE')

        self.frame_fields.grid(row=2,column=1,sticky='WE')

        self.icon_construct.grid(row=3,column=0,sticky='WE')
        self.lbl_construct.grid(row=3,column=1,columnspan=5,sticky='WE')

        self.frame_constructs.grid(row=4,column=1,columnspan=10, sticky='WE')

        # Decision Frame -> Connector Frame -> Expression Frame
        self.frame_decision.grid(column=0, row=1, columnspan=4, sticky='E')
        self.frame_connector.grid(column=0, row=2,columnspan=2, sticky='E')
        self.frame_expression.grid(column=0,row=3,columnspan=2, sticky='E')

    def init_fields(self):
        self.add_field("Start Field", col=0, row=1, im=self.im_circle, command=lambda : self.new_window(WindowType.WINDOW_START_FIELD))
        self.add_field("Field (1 byte)", col=1, row=1, command=lambda : self.new_window(WindowType.WINDOW_FIELD))

        self.add_field("Field (2 byte)", col=0, row=2, command=lambda : self.new_window(WindowType.WINDOW_FIELD))
        self.add_field("Field (4 byte)", col=1, row=2, command=lambda : self.new_window(WindowType.WINDOW_FIELD))

        self.add_field("Field (8 byte)", col=0, row=3, command=lambda : self.new_window(WindowType.WINDOW_FIELD))
        self.add_field("Field (16 byte)", col=1, row=3, command=lambda : self.new_window(WindowType.WINDOW_FIELD))

        self.add_field("Field (Var size)", col=0, row=4, command=lambda : self.new_window(WindowType.WINDOW_FIELD))
        self.add_field("End Field", col=1, row=4, im=self.im_circle, command=lambda : self.new_window(WindowType.WINDOW_END_FIELD))

        rlist = self.add_field("Reference List", col=0, row=5, command=lambda : self.new_window(WindowType.WINDOW_RLIST))
        pinfo = self.add_field("Packet Info.", col=1, row=5, command=lambda : self.new_window(WindowType.WINDOW_PINFO))

    def add_field(self, name, col, row, im=None, command=None):
        font = ("Helvetica", "10")
        if im is None:
            component = DragButton(self.frame_fields, text=name, command=command, font=font)
            component.config(width=10, height=1, bd=1)
        else:
            component = DragButton(self.frame_fields, text=name, command=command, image=im, compound=tk.CENTER, font=font, wraplength=50)

        component.grid(column=col, row=row)

        return component

    def init_constructs(self):
        self.init_decision_constructs()
        self.init_connector_constructs()
        self.init_expression_constructs()

    def init_decision_constructs(self):
        lbl_decision = tk.Label(self.frame_decision, text='Decision')
        lbl_decision.grid(column=0,row=0,sticky='W')

        btn_expression = DragButton(self.frame_decision, text='Expression', image=self.im_diamond, compound=tk.CENTER)
        btn_expression.grid(column=0,row=1)

    def init_connector_constructs(self):
        lbl = tk.Label(self.frame_connector, text='Connector')
        lbl.grid(column=0,row=0,sticky='WE')

        connector = DragButton(self.frame_connector, text='', image=self.im_arrow, compound=tk.CENTER, bg='white')
        connector.grid(column=0,row=1,sticky='WE')

    def init_expression_constructs(self):
        lbl = tk.Label(self.frame_expression, text='Expression')

        lbl2 = tk.Label(self.frame_expression, text='Relational Operator', bg='gray')
        op_frame1 = tk.Frame(self.frame_expression)
        op_less_than = DragButton(op_frame1, text='<')
        op_less_than_equal = DragButton(op_frame1, text='<=')
        op_greater_than = DragButton(op_frame1, text='>')
        op_greater_than = DragButton(op_frame1, text='>=')
        op_equal = DragButton(op_frame1, text='==')
        op_not_equal = DragButton(op_frame1, text='~=')

        lbl3 = tk.Label(self.frame_expression, text='Logical Operator')
        op_frame2 = tk.Frame(self.frame_expression)
        op_and = DragButton(op_frame2, text='And')
        op_or = DragButton(op_frame2, text='Or')
        op_not = DragButton(op_frame2, text='Not')

        operand = DragButton(self.frame_expression, text='Operand')

        lbl.grid(column=0,row=0,sticky='WE')
        lbl2.grid(column=0, row=1, sticky='WE')
        op_frame1.grid(column=0,row=2,sticky='WE')
        lbl3.grid(column=0, row=3, sticky='WE')
        op_frame2.grid(column=0, row=4)

        op_less_than.grid(column=1, row=0, sticky='WE')
        op_less_than_equal.grid(column=2, row=0, sticky='WE')
        op_greater_than.grid(column=3, row=0, sticky='WE')
        op_greater_than.grid(column=4, row=0, sticky='WE')
        op_equal.grid(column=5, row=0, sticky='WE')
        op_not_equal.grid(column=6, row=0, sticky='WE')

        op_and.grid(column=1,row=0,sticky='WE')
        op_or.grid(column=2,row=0,sticky='WE')
        op_not.grid(column=3,row=0,sticky='WE')

        operand.grid(column=0,row=7,sticky='WE')

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

class DBuilder(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # self.parent = parent
        # self.title('Dissector Builder Area')

        self.title_bar = TitleBar('Dissector Builder Area', self)
        self.title_bar.grid(column=0,row=0, columnspan=5, padx=1, pady=2, sticky='WE')

        self.frame_canvas = tk.Frame(self, bg='white')
        canvas = CanvasDnd(self.frame_canvas, bg='white', width=800, height=500)
        canvas.grid(column=0, row=1)
        tk.Label(self.frame_canvas, text='Canvas').grid(column=0, row=0, padx=2, pady=2)

        self.frame_palette = Palette(self)
        # self.frame_palette = tk.Frame(self, bg='red')
        # tk.Label(self.frame_palette, text='Palette').grid(column=0, row=0, columnspan=2)
        #
        # self.im = ImageTk.PhotoImage(Image.open('circular-shape-silhouette.png'))
        # lbl_field = tk.Label(self.frame_palette, text='Field', fg='white', image=self.im, compound=tk.CENTER)
        # lbl_field.grid(column=0, row=1)
        # lbl_field.bind('<ButtonPress>', self.on_dnd_start)

        # Layout
        self.frame_canvas.grid(column=0, row=1, sticky='WENS', padx=2, pady=2)
        self.frame_palette.grid(column=1, row=1, sticky='WENS', padx=2, pady=2)

class ProjectNavigation(tk.Frame):

    def label_clicked(self, event):
        if not self.FolderOpenA:
            self.folderpic = tk.PhotoImage(file="Openf.gif")
            self.sized_pic = self.folderpic.subsample(5, 5)
            self.label["image"] = self.sized_pic
            self.FolderOpenA=True
        else:
            self.folderpic = tk.PhotoImage(file="Closef.gif")
            self.sized_pic = self.folderpic.subsample(5, 5)
            self.label["image"] = self.sized_pic
            self.FolderOpenA = False

    def label_clickedB(self, event):
        if self.FolderOpenB==False:
            self.folderpic2 = tk.PhotoImage(file="Openf.gif")
            self.sized_pic2 = self.folderpic2.subsample(5, 5)
            self.label2["image"]=self.sized_pic2
            self.FolderOpenB=True
        else:
            self.folderpic2 = tk.PhotoImage(file="Closef.gif")
            self.sized_pic2 = self.folderpic2.subsample(5, 5)
            self.label2["image"]=self.sized_pic2
            self.FolderOpenB=False

    def label_clickedC(self, event):

        if self.FolderOpenC==False:

            self.folderpic3 = tk.PhotoImage(file="Openf.gif")
            self.sized_pic3 = self.folderpic3.subsample(5, 5)
            self.label3["image"]=self.sized_pic3
            self.FolderOpenC=True
        else:
            self.folderpic3 = tk.PhotoImage(file="Closef.gif")
            self.sized_pic3 = self.folderpic3.subsample(5, 5)
            self.label3["image"]=self.sized_pic3
            self.FolderOpenC=False

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.title_bar = TitleBar('Project Navigator', self)

        self.title_bar.bind()
        self.title_bar.pack(padx=2)
        #self.title_bar.pack(side='top', fill="x", expand=True)

        self.FolderOpenA=False
        self.FolderOpenB=False
        self.FolderOpenC = False

        self.label = tk.Label(self,text="WorkspaceX")
        self.label.bind()
        self.label.pack()

        self.folderpic = tk.PhotoImage(file="Closef.gif")
        self.sized_pic = self.folderpic.subsample(5, 5)
        self.label = tk.Label(self, text="ProjectA",compound='left',pady=10,padx=10)
        self.label.bind("<Button-1>", self.label_clicked)
        self.label["image"]=self.sized_pic
        self.label.pack()

        self.label2 = tk.Label(self, text="ProjectB",compound='left',pady=10,padx=10)
        self.label2.bind("<Button-1>", self.label_clickedB)
        self.folderpic2 = tk.PhotoImage(file="Closef.gif")
        self.sized_pic2 = self.folderpic2.subsample(5, 5)
        self.label2["image"]=self.sized_pic2
        self.label2.pack()

        self.label3 = tk.Label(self, text="ProjectC",compound='left',pady=10,padx=10)
        self.label3.bind("<Button-1>", self.label_clickedC)
        self.folderpic3 = tk.PhotoImage(file="Closef.gif")
        self.sized_pic3 = self.folderpic3.subsample(5, 5)
        self.label3["image"]=self.sized_pic3
        self.label3.pack()


class Workspace(tk.Tk):
    def new_window(self, type):
        if type == WindowType.WINDOW_WORKSPACE_LAUNCHER:
            form = WorkspaceLauncher(None)
        elif type == WindowType.WINDOW_NEW_PROJECT:
            form = NewProject(None)
        elif type == WindowType.WINDOW_DISSECTOR_SCRIPT:
            form = DissectorScript(None)
        elif type == WindowType.WINDOW_PROJECT_IMPORT:
            form = ProjectImport(None)
        elif type == WindowType.WINDOW_PROJECT_EXPORT:
            form = ProjectExport(None)
        elif type == WindowType.WINDOW_ORGANIZE_VIEWS:
            form = OrganizeViews(None)
        elif type == WindowType.WINDOW_OPEN_PCAP:
            form = PCAP(None)

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.title('Protocol Dissector Generator System')

        center = tk.Frame(self)
        top = tk.Frame(self)
        left = ProjectNavigation(self)
        center.grid(row=1,column=1, sticky='NEWS', padx=0, pady=2)
        top.grid(row=0,column=1, sticky='N', padx=2, pady=2)
        left.grid(row=1,column=0, sticky='NS', padx=1, pady=2)

        center_top = DBuilder(center)
        center_bottom = tk.Frame(center)
        psa = PacketStreamArea(center_bottom)
        dsa = DissectedStreamArea(center_bottom)
        rda = RawDataArea(center_bottom)
        ca = ConsoleArea(center_bottom)

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

if __name__ == '__main__':
    # FieldDialog(None).mainloop()
    # StartField(None).mainloop()
    # ReferenceListField(None).mainloop()
    # PacketInformationField(None).mainloop()
    # DBuilder(None).mainloop()
    Workspace(None).mainloop()