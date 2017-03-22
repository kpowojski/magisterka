#! /usr/bin/env python

from scapy.all import *

if __name__ == "__main__":
	pkts = rdpcap('/root/ipv6/caida_traffic/test.pcap')
	pkts[-1].show()
	count = 0
	for p in pkts:
		if p.version == 6:
			count = count + 1
			ihl = p.ihl
			print('ihl ', ihl)
			ip_src = p.src
			ip_dst = p.dst
			print(ip_src, ip_dst)
	print('Number of IPv6 packets ', count)
