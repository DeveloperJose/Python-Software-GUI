import Tkinter as tk
import Tkdnd
import copy

class Tree:
    current = None

    def __init__(self):
        self.fields = []

    def to_xml(self):
        pass

def MouseInWidget(Widget ,Event):
    x = Event.x_root - Widget.winfo_rootx()
    y = Event.y_root - Widget.winfo_rooty()
    return (x ,y)

class PaletteDraggable():
    def __init__(self, parent, frame):
        self.Canvas = None
        self.OriginalCanvas = None
        self.Label = None
        self.OriginalLabel = None

        self.OffsetX = 20
        self.OffsetY = 10

        self.Parent = parent
        self.Frame = frame

    def dnd_end(self, Target, Event):
        # self.Label.invoke()
        if self.Canvas == None and self.OriginalCanvas == None:
            return
        if self.Canvas == None and self.OriginalCanvas <> None:
            self.ID = self.OriginalID
            self.Label = self.OriginalLabel
            self.Canvas.dnd_enter(self, Event)
            return

        # At this point we know that self.Canvas is not None, which means we have an
        #    label of ourself on that canvas. Bind <ButtonPress> to that label so the
        #    the user can pick us up again if and when desired.
        self.Label.bind('<ButtonPress>', self.Press)
        # If self.OriginalCanvas exists then we were an existing object and our
        #    original label is still around although hidden. We no longer need
        #    it so we delete it.
        if self.OriginalCanvas:
            # info = Tree.current.fields[self.Frame]
            # lbl = self.OriginalLabel
            # print(self.OriginalLabel.test1.get())
            self.OriginalCanvas.delete(self.OriginalID)
            self.OriginalCanvas = None
            self.OriginalID = None
            self.OriginalLabel = None

    def Appear(self, Canvas, XY):
        if self.Canvas:
            return

        self.X, self.Y = XY
        if self.Frame is not None:
            info = Tree.current.fields[self.Frame]
            view = StartFieldView(Canvas, self.Frame)
            view.resurrect(info)
            self.Label = view
            #self.Label = info.create_view(Canvas, self.Frame)
        else:
            self.Label = tk.Label(Canvas, text='Hint')
        # Display the label on a window on the canvas. We need the ID returned by
        #    the canvas so we can move the label around as the mouse moves.
        self.ID = Canvas.create_window(self.X - self.OffsetX, self.Y - self.OffsetY, window=self.Label, anchor="nw")
        # Note the canvas on which we drew the label.
        self.Canvas = Canvas

    def Vanish(self, All=0):
        """
        If there is a label representing us on a canvas, make it go away.

        if self.Canvas is not None, that implies that "Appear" had prevously
            put a label representing us on the canvas and we delete it.

        if "All" is true then we check self.OriginalCanvas and if it not None
            we delete from it the label which represents us.
        """
        if self.Canvas:
            self.Canvas.delete(self.ID)
            self.Canvas = None
            del self.ID
            del self.Label

        if All and self.OriginalCanvas:
            # Delete label representing us from self.OriginalCanvas
            self.OriginalCanvas.delete(self.OriginalID)
            self.OriginalCanvas = None
            del self.OriginalID
            del self.OriginalLabel

    def Move(self, XY):
        assert self.Canvas, "Can't move because we are not on a canvas"
        self.X, self.Y = XY
        self.Canvas.coords(self.ID, self.X - self.OffsetX, self.Y - self.OffsetY)

    def Press(self, Event):
        # Save our current status
        self.OriginalCanvas = self.Canvas
        self.OriginalID = self.ID
        self.OriginalLabel = self.Label

        # Make phantom invisible
        self.Label.hide()

        # Say we have no current label
        self.ID = None
        self.Label = None
        self.Canvas = None

        # Ask Tkdnd to start the drag operation
        if Tkdnd.dnd_start(self, Event):
            # Save where the mouse pointer was in the label so it stays in the
            #    same relative position as we drag it around
            self.OffsetX, self.OffsetY = MouseInWidget(self.OriginalLabel, Event)
            # Draw a label of ourself for the user to drag around
            XY = MouseInWidget(self.OriginalCanvas, Event)
            self.Appear(self.OriginalCanvas, XY)

# class ViewManager():
#     def create_view(self, canvas, ID):
#         view = StartFieldView(canvas, ID)
#         view.resurrect(self)
#         return view

class StartFieldInfo():
    def __init__(self):
        self.protocol_name = ""
        self.protocol_desc = ""
        self.dependent_protocol_name = ""
        self.dependency_pattern = ""

class StartFieldView(tk.Canvas):
    def __init__(self, parent, ID):
        tk.Canvas.__init__(self, parent)
        self.parent = parent
        self.ID = ID

        self.frame = tk.Frame(self, bg='purple', width=100, height=100)

        # from titlebar import TitleBar
        # self.titlebar = TitleBar('StartField []', self.frame)
        # self.titlebar.grid(column=0, row=0)

        self.protocol_name = tk.StringVar()
        self.protocol_name.trace('w', self.update)
        self.entry_prot_name = tk.Entry(self.frame, textvariable=self.protocol_name)
        self.entry_prot_name.grid()

        self.create_window((65, 11), window=self.frame)

    def update(self, *args):
        info = Tree.current.fields[self.ID]
        info.protocol_name = self.protocol_name.get()

    def resurrect(self, info):
        self.protocol_name.set(info.protocol_name)

    def hide(self):
        self.configure(width=0,height=0)
        self.frame.configure(width=0,height=0)