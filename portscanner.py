import socket
import termcolor
import argparse


def scan(target, ports):
	print('\n' + ' Starting Scan For ' + target)
	for port in range(1,ports+1):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass


# targets = input("[*] Enter Targets To Scan(split them by ,): ")
# ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
parser=argparse.ArgumentParser()
parser.add_argument("target",help="Enter Single IP Address OR Enter Multiple IP Addresses To Scan [Keep Them Inside Of Double Quotes (\" \") and split them by ,] Example: \"10.10.10.11,10.10.10.13\"")
parser.add_argument("ports",help="Enter How Many Ports You Want To Scan, Examples: 'python3 portscanner.py 192.168.109.129 1024', 'python3 portscanner.py \"192.168.109.128,192.168.109.129,192.168.109.130\" 1024'")
args=parser.parse_args()
if ',' in args.target:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in args.target.split(','):
		scan(ip_addr.strip(),int(args.ports))
else:
	scan(args.target,int(args.ports))