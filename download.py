import os
import urllib2
import base64
import subprocess



username = 'wmazurczyk@tele.pw.edu.pl'
password = 'steg4ever'


baseurl_part1 = 'https://data.caida.org/datasets/passive-2016/equinix-chicago/20160406-130000.UTC/equinix-chicago.dirB.20160406-13'
baseurl_part2 = '00.UTC.anon.pcap.gz'

def create_url_list():
	url_list = []
	for i in range(30,59,1):
		url_list.append(baseurl_part1 + str(i) + baseurl_part2)
	return url_list

def download_file(https_path):
	print "##### Downloading file " + https_path.split('/')[-1] + " #####"  
	request = urllib2.Request(https_path)
	#base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
	request.add_header('Authorization', b'Basic ' +  base64.b64encode(username + b':' + password))

	request = urllib2.urlopen(request)
	data = request.read()
	with open('/root/ipv6/traffic/' +https_path.split('/')[-1] , 'wb') as pcap_file:
		pcap_file.write(data)

def download_file_with_wget(https_path):
	print "##### Downloading file (with wget) " + https_path.split('/')[-1] + " #####"
	args = ['wget', https_path, '--no-check-certificate', '--user', 'wmazurczyk@tele.pw.edu.pl', '--password', 'steg4ever', '--directory-prefix' , '/root/ipv6/traffic/']
	p = subprocess.Popen(args)
	stdout, stderr = p.communicate()
	print "##### Downloading finished #####"

def ungzip_file(sys_path):
	print "##### Ungzip file " + sys_path.split('/')[-1] + " #####"
	args = ['gunzip', sys_path]
	p = subprocess.Popen(args)
	stdout, stderr = p.communicate()
	print "#### Ungzip finished #####"
	

def extract_ipv6(sys_path, counter):
	file = sys_path.split('/')[-1]
	print "##### Extrating IPv6 traffic from " + file + " #####"
	args = ['tcpdump', 'ip6', '-r', sys_path,  '-w', '/root/ipv6/traffic/equinix-chicago.dirB.20160406.' + str(counter) + '.ipv6.pcap']
	p = subprocess.Popen(args)
	stdout, stderr = p.communicate()
	print stdout, stderr
	print "##### Extracting finished #####"


def delete_file(sys_path):
	print "##### Deleting PCAP file " + sys_path + " #####"
	try:
		os.remove(sys_path)
	except OSError:
		pass
	print '##### File deleted #####'




def main():
	url_list = create_url_list()
#	print url_list
#	print url_list[0].split('/')[-1]
#	delete_file('/root/ipv6/traffic/pcap.pcap')
#	extract_ipv6('/root/ipv6/traffic/equinix-chicago.dirB.20160406-134500-10-1000.UTC.anon.pcap', 1)


	counter = 0
	for num in range(6,20):
		download_file_with_wget(url_list[num])
		sys_path = '/root/ipv6/traffic/' + url_list[num].split('/')[-1]
		ungzip_file(sys_path)
		delete_file(sys_path)

		pcap_path = ".".join(sys_path.split('.')[:-1])
		extract_ipv6(pcap_path, counter)
		delete_file(pcap_path) 
		counter += 1
		print "Iteration " + str(counter)

def test():
	print ".".join('/root/ipv6/traffic/equinix-chicago.dirB.20160406-134500-10-1000.UTC.anon.pcap.gz'.split('.')[:-1])

if __name__ == "__main__":
	main()
#	test()
