import scapy.all as scapy 


scapy_cap = scapy.rdpcap('echo_chamber.pcap')
with open('output', 'wb') as f:
    for packet in scapy_cap:
        f.write(bytes(packet.payload)[28:])
