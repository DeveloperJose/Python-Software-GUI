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
