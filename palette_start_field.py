from table import Table

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