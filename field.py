import Tkinter as tk
from PIL import Image, ImageTk

class Table(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
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

        self.img_btn = ImageTk.PhotoImage(Image.open('plus-symbol-round-button.png'))
        self.btn_add = tk.Button(self, image=self.img_btn, command=self.on_btn_add)
        self.btn_add.grid(column=1, row=self.row + 1)

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

        self.img_btn = ImageTk.PhotoImage(Image.open('plus-symbol-round-button.png'))
        self.btn_add = tk.Button(self, image=self.img_btn, command=self.on_btn_add)
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

if __name__ == '__main__':
    # form = FieldDialog(None)
    # form = StartField(None)
    form = ReferenceListField(None)
    # form = PacketInformationField(None)
    form.mainloop()