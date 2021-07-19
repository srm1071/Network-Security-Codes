import socket
import sys
import string

HOST = ''	# Symbolic name meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port

# Datagram (udp) socket
try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print ('Socket created')
except socket.error as msg :
	print ('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()


# Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
	
print ('Socket bind complete')


#now keep talking with the client
try:
	# receive data from client (data, addr)
    d = s.recvfrom(1024)
    
   
    data = d[0]
    addr = d[1]
    data=d[0].decode()
    res = data.upper()
    t=res+'RR2014'
    print("Capitalized string",res, " is sent to client")
    s.sendto(t.encode(),addr)
    
    
	
#	if not data: 
#		break
	
	 
     
#	print ('Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip())
except socket.error as msg:
    print ('Error Code : ' + str(d[0]) + ' Message ' + d[1])
    sys.exit()
	
s.close()