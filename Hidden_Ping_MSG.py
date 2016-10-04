import argparse
import socket
from scapy.all import *
from time import sleep


def Craft_Packet(IP_dest, MSG, Spam):
	# Check IP
	STR = ''
	for i in MSG:
		STR += i
		STR += " "	
	try:
		socket.inet_aton(IP_dest)
	except:
		print("IP is not valid")
		return
	# Craft IP
	packet=IP(dst=IP_dest, ttl= 64)/ICMP()/Raw(load=STR)
	try:
		# If spam mode
		if(Spam):
			while 1:	
				reply=send(packet)
		else:
			reply=send(packet)
	except:
		# If exception
		print("Cannot send packet")	
	
def Hidden_Ping_MSG(args):
	# Simple parser 
	parser = argparse.ArgumentParser(description="Hide MSG in Ping data", usage=("Hidden_Ping -D destination_IP -M Message [-S]"))
	parser.add_argument("-D", action="store", dest="IP")
	parser.add_argument("-M", action="store", dest="Message", type=str, help="Only extended ASCII characters", nargs='*')
	parser.add_argument("-S", action="store_true", dest="Spam", help="Optionnal, Spam mode")
	
	try:
		# Split args
		options = parser.parse_args(args.split())
		IP = options.IP
		Spam = options.Spam
		Message = options.Message
		if not(IP):
			# If error using the crafter, print help
			print(parser.usage)
		else:
			# Craft Packet and send it
			Craft_Packet(IP, Message, Spam)
	except:
		print("Error.")
	
