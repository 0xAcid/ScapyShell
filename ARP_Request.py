import argparse
import socket
from scapy.all import *
from time import sleep

def Craft_Packet(IP_dest, IP_Source, HW_src, HW_dst):
	try:
		socket.inet_aton(IP_dest)
	except:
		print("IP is not valid")
		return
	trame = ARP()
	trame.pdst = IP_dest
	# Can be changed
	trame.hwsrc = HW_src
	trame.psrc =IP_Source
	# Can be changed
	trame.hwdst =HW_dst
	try:
		trame.display()
		send(trame)
	except:
		print("Cannot send packet.")

def ARP_Request(args):
	parser = argparse.ArgumentParser(description = "Send an ARP request", usage = ("ARP_Request -S source_IP -HS source_MAC -D destination_IP -HD destination_MAC"))
	parser.add_argument("-S", action = "store", dest = "IPsrc")
	parser.add_argument("-HS", action = "store", dest = "HWsrc")
	parser.add_argument("-HD", action = "store", dest = "HWdst")
	parser.add_argument("-D", action = "store", dest = "IPdst")
	try:
		options = parser.parse_args(args.split())
		IPsrc = options.IPsrc
		HWsrc = options.HWsrc
		HWdst = options.HWdst
		IPdst = options.IPdst
		if not(IPsrc) or not(IPdst) or not(HWdst) or not(HWsrc):
			print(parser.usage)
		else:
			Craft_Packet(IPdst, IPsrc, HWsrc, HWdst)
	except:
		print("Error.")
