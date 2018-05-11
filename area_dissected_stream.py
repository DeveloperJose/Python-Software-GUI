from area import TextWindow

class DissectedStreamArea(TextWindow):
    def __init__(self, *args, **kwargs):
        TextWindow.__init__(self, "Dissected Stream Area", *args, **kwargs)