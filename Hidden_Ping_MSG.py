import argparse
import socket
from scapy.all import *
from time import sleep


def Craft_Packet(IP_dest, MSG, Spam):
	try:
		socket.inet_aton(IP_dest)
	except:
		print("IP is not valid")
		return
	packet=IP(dst=IP_dest, ttl= 64)/ICMP()/Raw(load=MSG)
	try:
		if(Spam):
			while 1:	
				reply=send(packet)
		else:
			reply=send(packet)
	except:
		print("Cannot send packet")	
	
def Hidden_Ping_MSG(args):
	parser = argparse.ArgumentParser(description="Hide MSG in Ping data", usage=("Hidden_Ping -D destination_IP -M Message"))
	parser.add_argument("-D", action="store", dest="IP")
	parser.add_argument("-M", action="store", dest="Message", help="Only extended ASCII characters")
	parser.add_argument("-S", action="store_true", dest="Spam", help="Optionnal, Spam mode")
	
	try:
		options = parser.parse_args(args.split())
		IP = options.IP
		Spam = options.Spam
		Message = options.Message
		if not(IP):
			print(parser.usage)
		else:
			Craft_Packet(IP, Message, Spam)
	except:
		print("Error.")
	
