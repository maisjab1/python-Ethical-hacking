import scapy.all as scapy
import argparse
from scapy.layers import http

def parse():
    parser=argparse.ArgumentParser("HTTP Packet Sniffer — captures HTTP requests and POST data")
    parser.add_argument("-i", "--iface", dest="interface", required=True, help="Network interface to sniff on")
    args = parser.parse_args()
    interface = args.interface
    return interface

def process_sniffed_packet(packet):
        if packet.haslayer(http.HTTPRequest):
            host = packet[http.HTTPRequest].Host.decode(errors="ignore")
            path = packet[http.HTTPRequest].Path.decode(errors="ignore")
            method = packet[http.HTTPRequest].Method.decode(errors="ignore")
            print(f"\n[{method}] http://{host}{path}")
        
            if method == "POST" and  packet.haslayer(scapy.Raw):
                print("POST DATA:")
                print(packet[scapy.Raw].load.decode(errors="ignore"))
        elif packet.haslayer(scapy.Raw) and packet.haslayer(scapy.TCP):
            body = packet[scapy.Raw].load.decode(errors="ignore")
            if "=" in body and not body.startswith("HTTP"):
                print(f"[POST BODY] {body}")
interface = parse()
print(f"[*] Sniffing on {interface}...")

scapy.sniff(iface= interface , store=False, prn=process_sniffed_packet)
