#! /usr/bin/env python

from scapy.all import *
import pyshark
import time

traffic_class = []


def parse_with_scapy(path):
	pkts = rdpcap(path)
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


def parse_with_pcapy(path):
	pcap_file = pcapy.open_offline(path)
	count = 1
	(header, payload) = pcap_file.next()
	print header


def parse(pcap_file):
#       01 02 03 04 05 06 07 08  A  B  C  D  E  F  G  H

#0000   60 C0 00 00 05 8C 06 34  A6 FC A7 81 A1 CF 9E EA   `......4........
#0010   00 00 00 00 00 00 00 00  AD F6 67 18 67 FE C0 0E   ..........g.g...
#0020   00 00 00 00 00 00 00 00  01 BB E4 FD 5E 7D 7A A3   ............^}z.
#0030   71 2D 2B 6A 80 10 00 AE  9C C5 00 00 01 01 08 0A   q-+j............
	cap  = pyshark.FileCapture(pcap_file)
	print cap[0]['ipv6']
	print dir(cap[0].ip)



def main():
#	parse_with_scapy('/root/ipv6/traffic/equinix-chicago.dirB.7.ipv6.pcap')
#	read_with_scapy('/root/ipv6/traffic/equinix-chicago.dirB.7.ipv6.pcap')
	str_time = time.time()
	parse('/root/ipv6/traffic/equinix-chicago.dirA.7.ipv6.pcap')
	end_time = time.time()
	res = end_time - str_time

	print '#### Finished ####'
	print res
	return res

if __name__ == '__main__':
	main()
