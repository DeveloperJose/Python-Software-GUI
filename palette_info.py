import xml.etree.ElementTree as ET
class FieldInfo():
    def __init__(self):
        self.name = ""

    def to_xml(self, root):
        e = ET.SubElement(root, 'field')
        e.set('name', self.name)
        return e

    def __str__(self):
        return 'Field [%s]' % self.name

class ConnectorInfo():
    def __init__(self):
        self.src = None
        self.dst = None
        self.line_id = -1

    def to_xml(self, root):
        e = ET.SubElement(root, 'connector')
        e.set('src', self.src)
        e.set('dst', self.dst)
        e.set('line_id', self.line_id)
        return e

class StartFieldInfo():
    def __init__(self):
        self.proto_name = ""
        self.proto_desc = ""
        self.dep_proto_name = ""
        self.dep_pattern = ""

    def to_xml(self, root):
        e = ET.SubElement(root, 'start_field')
        e.set('proto_name', self.proto_name)
        e.set('proto_desc', self.proto_desc)
        e.set('dep_proto_name', self.dep_proto_name)
        e.set('dep_pattern', self.dep_pattern)
        return e

    def __str__(self):
       return 'Start Field [%s]' % self.proto_name

class EndFieldInfo():
    def __init__(self):
        pass

    def to_xml(self, root):
        e = ET.SubElement(root, 'end_field')
        return e

    def __str__(self):
        return 'End Field'