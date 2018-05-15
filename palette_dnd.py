import Tkinter as tk
import Tkdnd

from palette_info import StartFieldInfo, ConnectorInfo, FieldInfo, EndFieldInfo
from palette_view import FieldView, StartFieldView, ConnectorView, EndFieldView
from workspace import Workspace

def MouseInWidget(Widget ,Event):
    x = Event.x_root - Widget.winfo_rootx()
    y = Event.y_root - Widget.winfo_rooty()
    return (x ,y)

class Draggable():
    def __init__(self, parent, frame):
        self.Canvas = None
        self.OriginalCanvas = None
        self.Label = None
        self.OriginalLabel = None

        self.OffsetX = 20
        self.OffsetY = 10

        self.Parent = parent
        self.INFO_ID = frame

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

    def view_from_info(self, Canvas, info):
        if isinstance(info, StartFieldInfo):
            view = StartFieldView(Canvas, self.INFO_ID)
        elif isinstance(info, ConnectorInfo):
            view = ConnectorView(Canvas, self.INFO_ID)
        elif isinstance(info, FieldInfo):
            view = FieldView(Canvas, self.INFO_ID)
        elif isinstance(info, EndFieldInfo):
            view = EndFieldView(Canvas, self.INFO_ID)
        else:
            raise Exception('Info is not supported')
        view.resurrect(info)
        view.init_vars()
        return view

    def Appear(self, Canvas, XY):
        if self.Canvas:
            return

        self.X, self.Y = XY
        self.X = Canvas.canvasx(self.X)
        self.Y = Canvas.canvasy(self.Y)
        if self.INFO_ID is not None:
            info = Workspace.current.get_tree().fields[self.INFO_ID]
            self.Label = self.view_from_info(Canvas, info)
        else:
            raise Exception('Info_ID is None')
        # Display the label on a window on the canvas. We need the ID returned by
        #    the canvas so we can move the label around as the mouse moves.

        x = self.X - self.OffsetX
        y = self.Y - self.OffsetY
        self.ID = Canvas.create_window(x, y, window=self.Label, anchor="nw")
        # Note the canvas on which we drew the label.
        self.Canvas = Canvas

        self.Label.VIEW_ID = self.ID
        Workspace.current.get_tree().views[self.INFO_ID] = self.Label

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
        self.X = self.Canvas.canvasx(self.X)
        self.Y = self.Canvas.canvasy(self.Y)
        self.Canvas.coords(self.ID, self.X - self.OffsetX, self.Y - self.OffsetY)

    def Press(self, Event):
        # Save our current status
        self.OriginalCanvas = self.Canvas
        self.OriginalID = self.ID
        self.OriginalLabel = self.Label

        # Make phantom invisible
        self.Label.__hide__()

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