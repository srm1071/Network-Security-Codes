import socket
import sys
import pickle


HOST = ''   
PORT = 8888 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

s.listen(10)
print ('Socket now listening')

p=[]
conn, addr = s.accept()
print ('Connected with ' + addr[0] + ':' + str(addr[1]))
rcvdData = conn.recv(4096).decode()
print ("Client:",rcvdData)    
p.append('bye')
sendData=pickle.dumps(p)
print("Bye")
conn.send(sendData)
    
conn.close()
