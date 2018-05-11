from area import TextWindow

class ConsoleArea(TextWindow):
    def __init__(self, *args, **kwargs):
        TextWindow.__init__(self, "Console", *args, **kwargs)