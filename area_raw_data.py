from area import Area
import subprocess as sp
class AreaRawData(Area):
    def __init__(self, *args, **kwargs):
        Area.__init__(self, "Raw Data Area", *args, **kwargs)

    def get_raw(self, pcap_path):

        output = "No PCAP file"
        try:
            output = sp.check_output('tshark -r ' + pcap_path + ' -x')
        except:
            pass

        self.insert(output)
