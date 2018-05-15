from area import Area

class AreaRawData(Area):
    def __init__(self, *args, **kwargs):
        Area.__init__(self, "Raw Data Area", *args, **kwargs)