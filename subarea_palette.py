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
