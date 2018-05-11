from table import Table
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