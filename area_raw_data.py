from area import TextWindow

class RawDataArea(TextWindow):
    def __init__(self, *args, **kwargs):
        TextWindow.__init__(self, "Raw Data Area", *args, **kwargs)