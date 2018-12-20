import os
import sys
import ipaddress

from scapy.all import *


ip_range = sys.argv[1]
TIMEOUT = 2
conf.verb = 0
for ip in ipaddress.IPv4Network(ip_range):
    packet = IP(dst=ip, ttl=20)/ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    if not (reply is None):
         print reply.dst, "is online"
    else:
         print "Timeout waiting for %s" % packet[IP].dst
