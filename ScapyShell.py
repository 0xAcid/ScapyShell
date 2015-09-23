import argparse
import cmd
from Hidden_Ping_MSG import Hidden_Ping_MSG

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

def Head():
	print (HEADER + "######## Axi0m_S's Shell - Network ########" + ENDC)


class Shell(cmd.Cmd):
	def do_exit(self, line):
		exit(0)
		
	def do_Hidden_Ping_MSG(self, args):
		Hidden_Ping_MSG(args)
		
	def help_exit(self):
		print("Exit shell.")
	def help_Hidden_Ping_MSG(self):
		print("Send ping with hidden messages in it.")
		
	def emptyline(self):
         pass
		

if __name__ == '__main__':
	Head()
	Axi0m_S_Shell = Shell()
	Axi0m_S_Shell.prompt = OKBLUE + "Root@Ax:~# " + ENDC
	Axi0m_S_Shell.cmdloop("Welcome.\n")
	
