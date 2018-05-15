from project import Project, Tree
class Workspace():
    current = None

    def __init__(self, name):
        self.name = name
        self.projects = [Project('ICMP', 'ICMP Protocol', Tree()), Project('HTTP', 'HTTP Proto', Tree())]
        self.selected_project = 0

    def get_tree(self):
        return self.projects[self.selected_project].tree