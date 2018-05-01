class DragButton(tk.Button):
    def on_dnd_start(self, event, name, component):
        ThingToDrag = Dragged(name, component)
        Tkdnd.dnd_start(ThingToDrag, event)

    def __init__(self, parent, text, command=None, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.configure(text=text, command=command)
        self.bind('<ButtonPress>', lambda event: self.on_dnd_start(event, text, self))