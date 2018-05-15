from area import Area

class AreaConsole(Area):
    def __init__(self, *args, **kwargs):
        Area.__init__(self, "Console", *args, **kwargs)