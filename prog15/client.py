# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 09:49:54 2021

@author: Suraj
"""

import socket	#for sockets
import sys	#for exit


# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print ('Failed to create socket')
	sys.exit()

host = 'localhost';
port = 8888;

try :
    msg=input('Enter string : ')
		#Set the whole string
    s.sendto(msg.encode(), (host, port))
    t=s.recvfrom(1024)
    print ('Server reply : ',t[0].decode("utf-8"))
    sys.exit()
		
		# receive data from client (data, addr)
#		d = s.recvfrom(1024)
#		reply = d[0]
#		addr = d[1]

	
except socket.error as msg:
    print ('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
s.close()
