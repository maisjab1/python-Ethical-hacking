import subprocess
import optparse
import re
print("--------------- mac changer ------------")
def parse_args():

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to cahnge the mac")
    parser.add_option("-m", "--mac", dest="mac", help="new mac address")
    opt,args=parser.parse_args()
    interface=opt.interface
    mac=opt.mac
    if not interface:
        print("[-] please provide an interface")
        exit(0)
    elif  not re.fullmatch(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", mac):
        print("Invalid MAC address format")
        exit(0)
    elif not mac:
        print("[-] plaese provide mac")
        exit(0)
    else:
        return interface,mac
def change_mac(interface, mac):
    print(f"[+] changing interface {interface} mac  to {mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])
def get_current_mac(interface):
    res = subprocess.check_output(["ifconfig",interface])
    res = res.decode("utf-8")
    mac =re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",res)
    if mac:
        return mac.group(0)
    else:
        print("[-] could not read interface mac address")
        exit(0)
try:
    interface,mac=parse_args()
    current_mac=str(get_current_mac(interface))
    print(f"current mac-> {current_mac}")
    change_mac(interface, mac)
    new_mac=str(get_current_mac(interface))
    if new_mac == mac and new_mac!= current_mac:
        print("[+] mac changed successfully")
        print(f"changed mac-> {str(get_current_mac(interface))}")
    else:
        print("[-] mac did not change")
except Exception as e:
    print(e)
