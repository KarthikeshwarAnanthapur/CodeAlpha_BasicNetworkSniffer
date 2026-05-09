from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
from datetime import datetime

packet_count = 0


def packet_callback(packet):

    global packet_count
    packet_count += 1

    print("\n========================================")
    print(f"Packet Number : {packet_count}")
    print(f"Time          : {datetime.now()}")

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print(f"Source IP     : {src_ip}")
        print(f"Destination IP: {dst_ip}")

        # TCP Protocol
        if packet.haslayer(TCP):

            protocol = "TCP"

            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        # UDP Protocol
        elif packet.haslayer(UDP):

            protocol = "UDP"

            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        else:

            protocol = "Other"
            src_port = "-"
            dst_port = "-"

        print(f"Protocol      : {protocol}")
        print(f"Source Port   : {src_port}")
        print(f"Destination Port : {dst_port}")

        print(f"Packet Length : {len(packet)} bytes")

        # Payload preview
        if packet.payload:

            payload = bytes(packet.payload)

            print(f"Payload Preview: {payload[:50]}")

        # Save to file
        with open("packets.txt", "a") as file:

            file.write(f"""
Packet Number : {packet_count}
Time          : {datetime.now()}
Source IP     : {src_ip}
Destination IP: {dst_ip}
Protocol      : {protocol}
Source Port   : {src_port}
Destination Port : {dst_port}
Packet Length : {len(packet)} bytes
-----------------------------------
""")


# Capture only TCP and UDP packets
sniff(prn=packet_callback, count=10)