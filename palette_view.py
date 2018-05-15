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
    def __init__(self, master, INFO_ID):
        View.__init__(self, master, INFO_ID)
        self['bg'] = 'blue'
        self['width'] = 200
        self['height'] = 100

        # StringVars
        self.var_name = tk.StringVar()
        self.var_name.trace('w', self.__update__)

        self.entry_name = tk.Entry(self, textvariable=self.var_name)
        self.lbl_name = tk.Label(self, text='Name')

        self.create_window((120, 11), window=self.entry_name)
        self.create_window((20, 11), window=self.lbl_name)

    def update(self, info):
        info.name = self.var_name.get()

    def resurrect(self, info):
        self.var_name.set(info.name)

class StartFieldView(View):
    def init_vars(self):
        self.var_proto_name.trace('w', self.__update__)
        self.var_proto_desc.trace('w', self.__update__)
        self.var_dep_proto_name.trace('w', self.__update__)
        self.var_dep_pattern.trace('w', self.__update__)

    def __init__(self, master, INFO_ID):
        View.__init__(self, master, INFO_ID)
        self['bg'] = 'purple'
        self['height'] = 150

        self.titlebar = TitleBar(self, 'Start Field []')

        self.lbl_proto_name = tk.Label(self,text='Protocol Name')
        self.lbl_proto_desc = tk.Label(self,text='Protocol Description')
        self.lbl_dep_proto_name = tk.Label(self,text='Dependent Protocol Name')
        self.lbl_dep_pattern = tk.Label(self,text='Dependency Pattern')

        self.var_proto_name = tk.StringVar(self)
        self.var_proto_desc = tk.StringVar(self)
        self.var_dep_proto_name = tk.StringVar(self)
        self.var_dep_pattern = tk.StringVar(self)

        self.entry_proto_name = tk.Entry(self, textvariable=self.var_proto_name, width=40)
        self.entry_proto_desc = tk.Entry(self, textvariable=self.var_proto_desc, width=40)
        self.entry_dep_proto_name = tk.Entry(self, textvariable=self.var_dep_proto_name, width=35)
        self.entry_dep_pattern = tk.Entry(self, textvariable=self.var_dep_pattern, width=35)

        self.create_window((320, 12), window=self.titlebar)
        self.create_window((47, 50), window=self.lbl_proto_name)
        self.create_window((250, 50), window=self.entry_proto_name)
        self.create_window((60, 70), window=self.lbl_proto_desc)
        self.create_window((250, 70), window=self.entry_proto_desc)
        self.create_window((76, 90), window=self.lbl_dep_proto_name)
        self.create_window((265, 90), window=self.entry_dep_proto_name)
        self.create_window((60, 110), window=self.lbl_dep_pattern)
        self.create_window((250, 117), window=self.entry_dep_pattern)

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

class ConnectorView(View):
    def __init__(self, master, INFO_ID):
        View.__init__(self, master, INFO_ID)

        self['bg'] = 'red'
        self['height'] = 100

        from titlebar import TitleBar
        self.titlebar = TitleBar(self, 'Connector {src->dst}')

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
        self.create_window((320, 12), window=self.titlebar)
        self.create_window((65, 20), window=self.src)
        self.create_window((65, 40), window=self.dst)

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
        self.titlebar.title.set("Connector {%s->%s}" % (info.src, info.dst))

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
