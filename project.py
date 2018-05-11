class Project():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    @staticmethod
    def load_from_xml(xml):
        if xml is None:
            return None

        return Project('','')