import subprocess
import os



def get_file_names():
	files = []
	for file in os.listdir('/root/ipv6/traffic'):
		files.append(file)
	return files



def rename_file():
	files = get_file_names()
	for f in files:
		name = f.split('.')
		nname = ".".join(name[:-4]) + "."  + str(int(name[-3]) + 5) + "." + ".".join(name[-2:])
		print nname
		args = ['mv', '/root/ipv6/traffic/'+f, '/root/ipv6/traffic/'+nname]
		p = subprocess.Popen(args)
		stdout, stderr = p.communicate()

def main():
	rename_file()


if __name__ == '__main__':
	main()
