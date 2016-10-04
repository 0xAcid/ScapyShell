import argparse
import cmd
from Hidden_Ping_MSG import Hidden_Ping_MSG
from ARP_Request import ARP_Request
try:
	import readline
except:
	print("Try installing readline if you got trouble with autocompletion etc..")

# GLOBAL VARIABLES
# Theses are colors, used or Unix systems
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
# Get system environment

# Shell Header
def Head():
	print (HEADER + "######## Scapy Shell - Network ########" + ENDC)

class Shell(cmd.Cmd):
	# Exit
	def do_exit(self, line):
		exit(0)
		
	# Hide message in Ping	
	def do_Hidden_Ping_MSG(self, args):
		Hidden_Ping_MSG(args)
        # Do an ARP Request
	def do_ARP_Request(self, args):
		ARP_Request(args)
	# Exit help
	def help_exit(self):
		print("Exit shell.")
		
	# Hidden Ping help
	def help_Hidden_Ping_MSG(self):
		print("Send ping with hidden messages in it.")
	# ARP Request help
	def help_ARP_Request(self):
		print("Send an ARP request with custom parameters")
	def emptyline(self):
         pass
		

if __name__ == '__main__':
	Head()
	# Start shell
	Axi0m_S_Shell = Shell()
	Axi0m_S_Shell.prompt = OKBLUE + "Root@Scap:~# " + ENDC
	Axi0m_S_Shell.cmdloop("Welcome.\n")
	
