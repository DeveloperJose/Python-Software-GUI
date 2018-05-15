import Tkinter as tk
from workspace import Workspace
from titlebar import TitleBar
from palette_info import ConnectorInfo
class View(tk.Canvas):
    def __init__(self, master, INFO_ID):
        tk.Canvas.__init__(self, master)
        self.ID = INFO_ID
        self.VIEW_ID = -1

    def init_vars(self):
        pass

    def update(self, info):
        pass

    def resurrect(self, info):
        pass

    def __update__(self, *args):
        info = Workspace.current.get_tree().fields[self.ID]
        self.update(info)

    def __hide__(self):
        self.configure(width=0,height=0)
        self.delete(tk.ALL)

class FieldView(View):
    def init_vars(self):
        self.var_name.trace('w', self.__update__)
        self.var_abbreviation.trace('w', self.__update__)
        self.var_description.trace('w', self.__update__)
        self.var_datatype.trace('w', self.__update__)
        self.var_base.trace('w', self.__update__)
        self.var_vc.trace('w', self.__update__)
        self.var_required.trace('w', self.__update__)

    def __init__(self, master, INFO_ID):
        View.__init__(self, master, INFO_ID)
        self['height'] = 210

        self.titlebar = TitleBar(self, 'Field []')

        self.var_name = tk.StringVar()
        self.var_abbreviation = tk.StringVar()
        self.var_description = tk.StringVar()
        self.var_datatype = tk.StringVar()
        self.var_base = tk.StringVar()
        self.var_vc = tk.StringVar()
        self.var_required = tk.StringVar()

        self.proto_name_label = tk.Label(text="Name")
        self.entry_name = tk.Entry(self, textvariable=self.var_name, width=40)
        self.abbr_label = tk.Label(text="Abbreviation")
        self.abbr_entry = tk.Entry(self, textvariable=self.var_abbreviation, width=40)
        self.desc_label = tk.Label(text="Description")
        self.desc_entry = tk.Entry(self, textvariable=self.var_description, width=40)
        self.datatype_list = (
        'types.NONE', 'ftypes.PROTOCOL', 'ftypes.BOOLEAN', 'ftypes.UINT8', 'ftypes.UINT16', 'ftypes.UINT24',
        'ftypes.UINT32', 'ftypes.UINT64', 'ftypes.INT8', 'ftypes.INT16', 'ftypes.INT24', 'ftypes.INT32', 'ftypes.INT64',
        'ftypes.FLOAT', 'ftypes.DOUBLE', 'ftypes.ABSOLUTE_TIME', 'ftypes.RELATIVE_TIME', 'ftypes.STRING',
        'ftypes.STRINGZ', 'ftypes.UINT_STRING', 'ftypes.ETHER', 'ftypes.BYTES', 'ftypes.UINT_BYTES', 'ftypes.IPv4',
        'ftypes.IPv6', 'ftypes.IPXNET', 'ftypes.FRAMENUM', 'ftypes.PCRE', 'ftypes.GUID', 'ftypes.OID', 'ftypes.EUI6')
        self.var_datatype.set(self.datatype_list[0])
        self.entry_datatype = tk.OptionMenu(self, self.var_datatype, *self.datatype_list)
        self.datatype_label = tk.Label(text="Datatype")
        self.base_label = tk.Label(text="Base")
        self.base_list = ('base.NONE', 'base.DEC', 'base.HEX', 'base.OCT', 'base.DEC_HEX', 'base.HEX_DEC')
        self.var_base.set(self.base_list[0])
        self.entry_base = tk.OptionMenu(self, self.var_base, *self.base_list)
        self.vc_label = tk.Label(text="Value Constraint")
        self.vc_entry = tk.Entry(self, textvariable=self.var_vc, width=40)
        self.required_label = tk.Label(text="Required")
        self.required_list = ('Yes', 'No')
        self.var_required.set(self.required_list[0])
        self.required_entry = tk.OptionMenu(self, self.var_required, *self.required_list)

        self.create_window((47, 50), window=self.proto_name_label)
        self.create_window((190, 12), width=380, window=self.titlebar)
        self.create_window((250, 50), window=self.entry_name)
        self.create_window((38, 70), window=self.abbr_label)
        self.create_window((250, 70), window=self.abbr_entry)
        self.create_window((35, 90), window=self.desc_label)
        self.create_window((250, 90), window=self.desc_entry)
        self.create_window((250, 118), window=self.entry_datatype)
        self.create_window((28, 118), window=self.datatype_label)
        self.create_window((17, 140), window=self.base_label)
        self.create_window((250, 145), window=self.entry_base)
        self.create_window((45, 170), window=self.vc_label)
        self.create_window((250, 170), window=self.vc_entry)
        self.create_window((28, 196), window=self.required_label)
        self.create_window((250, 196), window=self.required_entry)

    def update(self, info):
        info.name = self.var_name.get()
        info.abbreviation = self.var_abbreviation.get()
        info.description = self.var_description.get()
        info.reference_list = ''
        info.data_type = self.var_datatype.get()
        info.base = self.var_base.get()
        info.mask = ''
        info.value_constraint = self.var_vc.get()
        info.required = self.var_required.get()

        self.titlebar.title.set('Field [%s]' % info.name)

    def resurrect(self, info):
        self.var_name.set(info.name)
        self.var_abbreviation.set(info.abbreviation)
        self.var_description.set(info.description)
        self.var_datatype.set(info.data_type)
        self.var_base.set(info.base)
        self.var_vc.set(info.value_constraint)
        self.var_required.set(info.required)

        self.titlebar.title.set('Field [%s]' % info.name)

class StartFieldView(View):
    def init_vars(self):
        self.var_proto_name.trace('w', self.__update__)
        self.var_proto_desc.trace('w', self.__update__)
        self.var_dep_proto_name.trace('w', self.__update__)
        self.var_dep_pattern.trace('w', self.__update__)

    def __init__(self, master, INFO_ID):
        View.__init__(self, master, INFO_ID)
        self['height'] = 150

        self.titlebar = TitleBar(self, 'Start Field []')

        self.protocol_name_label = tk.Label(text='Protocol Name')
        self.var_proto_name = tk.StringVar()
        self.entry_proto_name = tk.Entry(self, textvariable=self.var_proto_name, width=40)

        self.create_window((47,50),window=self.protocol_name_label)
        self.create_window((190, 10), width=380, window=self.titlebar)
        self.create_window((250, 50), window=self.entry_proto_name)

        self.protocol_desc_label = tk.Label(text='Protocol Description')
        self.var_proto_desc = tk.StringVar()
        self.entry_proto_desc = tk.Entry(self, textvariable=self.var_proto_desc, width=40)

        self.create_window((60,70), window=self.protocol_desc_label)
        self.create_window((250,70), window= self.entry_proto_desc)
################
        self.protocol_dpn_label = tk.Label(text='Dependent Protocol Name')
        self.var_dep_proto_name = tk.StringVar()
        self.entry_dep_proto_name = tk.Entry(self, textvariable=self.var_dep_proto_name, width=35)

        self.create_window((76, 90), window=self.protocol_dpn_label)
        self.create_window((265, 90), window=self.entry_dep_proto_name)
#################
        self.dp_label = tk.Label(text='Dependency Pattern')
        self.var_dep_pattern = tk.StringVar()
        self.entry_dp = tk.Entry(self, textvariable=self.var_dep_pattern, width=40)

        self.create_window((60, 110), window=self.dp_label)
        self.create_window((250, 117), window=self.entry_dp)
        self['height']=150

    def update(self, info):
        info.proto_name = self.var_proto_name.get()
        info.proto_desc = self.var_proto_desc.get()
        info.dep_proto_name = self.var_dep_proto_name.get()
        info.dep_pattern = self.var_dep_pattern.get()

        self.titlebar.title.set('Start Field [%s]' % info.proto_name)

    def resurrect(self, info):
        self.var_proto_name.set(info.proto_name)
        self.var_proto_desc.set(info.proto_desc)
        self.var_dep_proto_name.set(info.dep_proto_name)
        self.var_dep_pattern.set(info.dep_pattern)
        self.titlebar.title.set('Start Field [%s]' % info.proto_name)

class EndFieldView(View):
    def __init__(self, master, INFO_ID):
        View.__init__(self, master, INFO_ID)
        self['height']=30
        self['width']=150
        self.title_bar = TitleBar(self, 'End Field')

        self.create_window((75,12),width=150,window=self.title_bar)

    def update(self, *args):
        pass

    def resurrect(self, info):
        pass

class ConnectorView(View):
    def __init__(self, master, INFO_ID):
        View.__init__(self, master, INFO_ID)

        self['bg'] = 'red'
        self['height'] = 100
        self['width'] = 300

        from titlebar import TitleBar
        self.titlebar = TitleBar(self, 'Connector')

        # StringVars
        self.var_src = tk.StringVar(self, 'None')
        self.var_dst = tk.StringVar(self, 'None')
        self.src_idx = -1
        self.dst_idx = -1

        # Components
        self.arrow = tk.Label()

        self.src = tk.OptionMenu(self, self.var_src, None)
        self.src.bind('<Button-1>', self.on_menu_open)

        self.dst = tk.OptionMenu(self, self.var_dst, None)
        self.dst.bind('<Button-1>', self.on_menu_open)

        # Layout
        self.create_window((101, 10), width=400, window=self.titlebar)
        self.create_window((65, 40), window=self.src)
        self.create_window((65, 80), window=self.dst)

    def on_menu_open(self, event):
        menu_src = self.src["menu"]
        menu_src.delete(0, "end")
        menu_dst = self.dst["menu"]
        menu_dst.delete(0, "end")

        for i in range(len(Workspace.current.get_tree().fields)):
            info = Workspace.current.get_tree().fields[i]
            if isinstance(info, ConnectorInfo):
                continue
            option = str(info)

            menu_src.add_command(label=option, command=lambda option=option: self.var_src.set(option))
            menu_dst.add_command(label=option, command=lambda option=option: self.var_dst.set(option))

    def update(self, info):
        info.src = self.var_src.get()
        info.dst = self.var_dst.get()
        self.update_line(info)
        # self.titlebar.title.set("Connector {%s->%s}" % (info.src, info.dst))

    def update_line(self, info):
        if info.src != 'None' and info.dst != 'None':
            src_idx = next((i for i in range(len(Workspace.current.get_tree().fields)) if str(Workspace.current.get_tree().fields[i]) == info.src), -1)
            dst_idx = next((i for i in range(len(Workspace.current.get_tree().fields)) if str(Workspace.current.get_tree().fields[i]) == info.dst), -1)
            if src_idx != -1 and dst_idx != -1:
                src_view = Workspace.current.get_tree().views[src_idx]
                dst_view = Workspace.current.get_tree().views[dst_idx]

                (x1, y1) = self.master.coords(src_view.VIEW_ID)
                (x2, y2) = self.master.coords(dst_view.VIEW_ID)

                x1 += src_view.winfo_width() / 2
                y1 += src_view.winfo_height()
                x2 += dst_view.winfo_width() / 2

                if info.line_id != -1:
                    self.master.delete(info.line_id)

                import random
                info.line_id = self.master.create_line(x1, y1, x2, y2,
                                                       arrow=tk.LAST, smooth=True,
                                                       arrowshape=(30,28,6),
                                                       width=1, fill="#" + ("%06x" % random.randint(0, 16777215)))

    def resurrect(self, info):
        self.var_src.set(info.src)
        self.var_dst.set(info.dst)
        self.update_line(info)
        self.titlebar.title.set("Connector {%s->%s}" % (info.src, info.dst))

    def init_vars(self):
        self.var_src.trace('w', self.__update__)
        self.var_dst.trace('w', self.__update__)
