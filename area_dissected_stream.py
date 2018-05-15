from area import Area

class AreaDissectedStream(Area):
    def __init__(self, *args, **kwargs):
        Area.__init__(self, "Dissected Stream Area", *args, **kwargs)