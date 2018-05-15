from area import Area
class AreaPacketStream(Area):
    def __init__(self, *args, **kwargs):
        Area.__init__(self, "Packet Stream Area", *args, **kwargs)