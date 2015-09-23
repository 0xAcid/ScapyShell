import argparse
import socket
from scapy.all import *


def Craft_Packet(IP_dest, MSG):
	try:
		socket.inet_aton(IP_dest)
	except:
		print("IP is not valid")
		return
	packet=IP(dst=IP_dest, ttl=64)/ICMP()/Raw(load=MSG)
	reply=send(packet)
def Hidden_Ping_MSG(args):
	parser = argparse.ArgumentParser(description="Hide MSG in Ping data", usage=("Hidden_Ping -D destination_IP -M Message"))
	parser.add_argument("-D", action="store", dest="IP")
	parser.add_argument("-M", action="store", dest="Message", help="Only extended ASCII characters")
	
	
	options = parser.parse_args(args.split())
	IP = options.IP
	Message = options.Message
	if not(IP):
		print(parser.usage)
	else:
		Craft_Packet(IP, Message)
		#print("IP : " + IP + "Options : "+ Message)
	
