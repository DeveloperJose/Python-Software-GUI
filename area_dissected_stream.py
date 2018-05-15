from area import Area
import subprocess as sp
class AreaDissectedStream(Area):
    def __init__(self, *args, **kwargs):
        Area.__init__(self, "Dissected Stream Area", *args, **kwargs)

    def get_info(self, pcap_path, lua_script_path):
        text = sp.check_output('tshark -r ' + pcap_path + ' -X lua_script:' + lua_script_path)
        self.insert(text)
