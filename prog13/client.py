import socket   
import sys  
import pickle

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print ('Failed to create socket')
    sys.exit()
    
print ('Socket Created')

host = '127.0.0.1';
port = 8888;

try:
    remote_ip = socket.gethostbyname( host )

except socket.gaierror:
    
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

s.connect((remote_ip , port))

try :
    str = input("Client: ")
    s.send(str.encode())
    data=s.recv(1024)
    t=pickle.loads(data)
    if(t[0]=='bye'):
      sys.exit()  
    else:
        print(t[0])
         
except socket.error:
    print ('Send failed')
    sys.exit()

s.close()
