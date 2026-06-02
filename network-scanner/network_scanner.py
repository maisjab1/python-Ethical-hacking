import scapy.all as scapy
import optparse


def parse():
    parser=optparse.OptionParser()
    parser.add_option("-t","--target", dest="ip", help="IP adress or range to discover")
    opt,args=parser.parse_args()
    target=opt.ip
    if not target:
        print("[-]please provide a target ip")
        exit(0)
    return target
def scan(target):
    arp_req= scapy.ARP(pdst=target)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_req
    answered,unanswered =scapy.srp(arp_req_broadcast,timeout=1,verbose=False)
    print("     IP                      MAC ADDRESS")
    print("     -----------------------------------------")
    for element in answered:
        print(f"    {element[1].psrc}",end="         ")
        print(f"    {element[1].hwsrc}")
try:
    target = parse()
    print("\n\n     ***           Network Scanner          ***\n\n")
    scan(target)
except Exception as e:
    print(e)
