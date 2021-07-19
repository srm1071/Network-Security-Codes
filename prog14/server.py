import socket
import sys
import pickle


HOST = ''   
PORT = 8888 

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

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
sendData= reverse(str(rcvdData))  
p.append(sendData)
sendData=pickle.dumps(p)

conn.send(sendData)
    
conn.close()
