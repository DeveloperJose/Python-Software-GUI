from area import Area
import subprocess as sp
from titlebar import TitleBar
import xml.etree.ElementTree as ET
import Tkinter as tk

class PacketStreamItem:
    def __init__(self):
        self.number = 0
        self.time = 0
        self.source = ""
        self.destination = ""
        self.protocol = ""
        self.info = ""

class AreaPacketStream(Area):
    def __init__(self, *args, **kwargs):
        Area.__init__(self, "Packet Stream Area", *args, **kwargs)

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.title_bar = TitleBar(self, "Packet Stream Area")
        self.table = tk.Frame(self)

        number = tk.Button(self.table, text="No.")
        time = tk.Button(self.table, text="Time")
        source = tk.Button(self.table, text="Source")
        destination = tk.Button(self.table, text="Destination")
        protocol = tk.Button(self.table, text="Protocol")
        info = tk.Button(self.table, text="Info")

        number.grid(row=0, column=0, sticky="E W")
        time.grid(row=0, column=1, sticky="E W")
        source.grid(row=0, column=2, sticky="E W")
        destination.grid(row=0, column=3, sticky="E W")
        protocol.grid(row=0, column=4, sticky="E W")
        info.grid(row=0, column=5, sticky="E W")

        self.table.grid(row=1, column=0)

        # self.grid(column=0, row=1)
        self.title_bar.set_max(lambda: self.table.grid())
        self.title_bar.set_min(lambda: self.table.grid_forget())

        self.title_bar.grid(column=0, row=0, sticky="E W")

        ##########################################################


        pcap_path = "C:\\Users\\xeroj\Desktop\\Local_Programming\\Python-Software-GUI\\example\\icmp.pcap"
        lua_path = "C:\\Users\\xeroj\Desktop\\Local_Programming\\Python-Software-GUI\\example\\icmp.lua"
        # self.fill_table(text)


        pdmltext = sp.check_output("tshark -r " + pcap_path + " -T pdml -X lua_script:" + lua_path)
        packets_info = self.get_packet_info("text.pdml", pdmltext)

        self.fill_table(packets_info)

    def get_packet_info(self, name, pdmltext):

        file = open(name, 'w')
        file.write(pdmltext)
        file.close()

        tree = ET.parse(name)
        root = tree.getroot()
        number = 0

        packets = []

        for packet in root:
            packet_info = PacketStreamItem()
            for proto in packet:
                if proto.attrib['name'] == 'ip':
                    for field in proto:
                        if field.attrib['name'] == 'ip.proto':
                            packet_info.protocol = field.attrib['showname'].split(' ')[1]

                if proto.attrib['name'] == 'frame':
                    for field in proto:
                        if field.attrib['name'] == 'frame.time_delta':
                            packet_info.time = field.attrib['show']

                if proto.attrib['name'] == 'ip':
                    attr = proto.attrib["showname"].split(',')
                    packet_info.source = attr[1].split(' ')[2]
                    packet_info.destination = attr[2].split(' ')[2]

            packet_info.number = number
            number += 1
            packets.append(packet_info)

        return packets

    def fill_table(self, packets_info):

        count = 1

        for info in packets_info:
            number_label = tk.Label(self.table, text=info.number)
            time_label = tk.Label(self.table, text=info.time)
            source_label = tk.Label(self.table, text=info.source)
            dest_label = tk.Label(self.table, text=info.destination)
            protocol_label = tk.Label(self.table, text=info.protocol)

            number_label.grid(row=count, column=0)
            time_label.grid(row=count, column=1)
            source_label.grid(row=count, column=2)
            dest_label.grid(row=count, column=3)
            protocol_label.grid(row=count, column=4)

            count += 1