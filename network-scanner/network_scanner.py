import scapy.all as scapy
import optparse


def parse():
    parser=optparse.OptionParser()
    parser.add_option("--ip", dest="ip", help="IP adress or range to discover")
    opt,args=parser.parse_args()
    ip=opt.ip
    if not ip:
        print("[-]please provide an IP")
        exit(0)
    return ip
def scan(ip):
    arp_req= scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_req
    answered,unanswered =scapy.srp(arp_req_broadcast,timeout=1,verbose=False)
    print("     IP                      MAC ADDRESS")
    print("     -----------------------------------------")
    for element in answered:
        print(f"    {element[1].psrc}",end="         ")
        print(f"    {element[1].hwsrc}")
try:
    ip=parse()
    print("\n\n     ***           Network Scanner          ***\n\n")
    scan(ip)
except Exception as e:
    print(e)
