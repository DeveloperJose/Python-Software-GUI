import Tkinter as tk

from PIL import Image, ImageTk

from table import Table


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