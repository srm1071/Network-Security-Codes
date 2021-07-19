import Pyro4

@Pyro4.expose
class RMIEchoServer(object):

    def __init__(self, name_server, host='localhost', port=9090):
        self.aMessages = list()
        self.name_server = name_server
        self.host = host
        self.port = port

    def sendMessageToReplicas(self, name_server, message):
        ns = Pyro4.locateNS(host=self.host,port=self.port) # find the name server)
        server_names = ns.list('rmiserver-') #this should be returning me all servers registered on pyro's nameserver
        keys = list(server_names.keys())

        for key in keys:
            each_server = Pyro4.Proxy(server_names[key])
            try:
                each_server.receiveMessageToReplica(name_server, message)
            except Pyro4.errors.CommunicationError:
                print('Can\'t send message to server ' + key.split('rmiserver-')[1])

    def receiveMessageToReplica(self, name_server, message):
        print('Received message from server ' + name_server)
        self.aMessages.append(message)

    def echoService(self, message):
        self.sendMessageToReplicas(self.name_server, str(message))
        print('Someone called my add method :)')
        message1=message[0] + message[1]
        message2=message[0] - message[1]
        message3=message1*message2
        return "addition is: "+ str(message1) + " "+"substraction is:"+str(message2)+" "+"multiply of results are: "+ " "+str(message3)