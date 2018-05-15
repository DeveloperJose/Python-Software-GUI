from palette_info import StartFieldInfo, ConnectorInfo, FieldInfo
import xml.etree.ElementTree as ET
class Project():
    def __init__(self, name, desc, tree):
        self.name = name
        self.desc = desc
        self.tree = tree

    @staticmethod
    def load_from_xml(xml):
        if xml is None:
            return None

        return Project('','')

    def __str__(self):
        return 'Project [%s]' % self.name

class Tree:
    # current = None

    def __init__(self):
        self.fields = []
        self.views = {}

    def __prettify__(self, elem):
        from xml.etree import ElementTree
        from xml.dom import minidom
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def to_xml(self):
        root = ET.Element('tree')
        for i in range(len(self.fields)):
            info = self.fields[i]
            info.to_xml(root)
        return self.__prettify__(root)