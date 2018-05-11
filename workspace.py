class Workspace():
    current = None

    def __init__(self, name):
        self.name = name
        self.projects = []