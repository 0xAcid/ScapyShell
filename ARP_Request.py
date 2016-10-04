import argparse
import socket
from scapy.all import *
from time import sleep

def Craft_Packet(IP_dest, IP_Source):
    try:
        socket.inet_aton(IP_dest)
    except:
        print("IP is not valid")
        return
    trame = ARP()
    trame.pdst = IP_dest
    # Can be change
    trame.hwsrc = "11:11:11:11:11:11"
    trame.psrc =IP_Source
    # Can be change
    trame.hwdst = "ff:ff:ff:ff:ff:ff"
    try:
        trame.display()
        send(trame)
    except:
        print("Cannot send packet.")

def ARP_Request(args):
    parser = argparse.ArgumentParser(description = "Send an ARP request", usage = ("ARP_Request -S source_IP -D destination_IP"))
    parser.add_argument("-S", action = "store", dest = "IPsrc")
    parser.add_argument("-D", action = "store", dest = "IPdst")
    try:
        options = parser.parse_args(args.split())
        IPsrc = options.IPsrc
        IPdst = options.IPdst
        if not(IPsrc) and not(IPdst):
            print(parser.usage)
        else:
            Craft_Packet(IPsrc, IPdst)
    except:
        print("Error.")
