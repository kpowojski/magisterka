import pyshark




def analyze(pcap_file):
	ecn = 4 * [0]
	diff_serv = 64 * [0]	
	flow_label = 2 * [0]
	next_header = 256 * [0]
	hop_limit = 256 * [0]
	pcap = pyshark.FileCapture(pcap_file)
	for pkt in pcap:
		#getting ecn from header
		e = int(pkt['ipv6'].tclass_ecn,10)
		ecn[e] += 1

		#getting diff_serv from header
		d = int(pkt['ipv6'].tclass_dscp, 10)
		diff_serv[d] += 1

		#getting flow_label
		f = pkt['ipv6'].flow
		if int(f[2:],16) == 0:
			flow_label[0] += 1
		else:
			flow_label[1] += 1

		#getting next_header from header
		n = int(pkt['ipv6'].nxt, 10)
		next_header[n] += 1

		#getting hop limit
		h = int(pkt['ipv6'].hlim, 10)
		hop_limit[h] +=  1 
	return ecn, diff_serv, flow_label, next_header, hop_limit

def save_to_file(output_file, list_name, list):
	output_file.write(list_name+ '\n')
	nl = [str(i) for i in list]
	s = ", ".join(nl)
	output_file.write(s + '\n')



def main():
	pcap_file = '/root/ipv6/traffic/equinix-chicago.dirA.1.ipv6.pcap'
	ecn, diff_serv, flow_label, next_header, hop_limit =  analyze(pcap_file)
	with open('/root/ipv6/traffic/analyst_1.txt', 'w') as output_file:
		save_to_file(output_file, 'ECN', ecn)
		save_to_file(output_file, 'DIFF serv', diff_serv)
		save_to_file(output_file, 'Flow label', flow_label)
		save_to_file(output_file, 'next header', next_header)
		save_to_file(output_file, 'hop limit', hop_limit)



if __name__ == '__main__':
	main()
