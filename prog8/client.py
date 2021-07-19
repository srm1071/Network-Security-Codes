import Pyro4
import os
import sys

HOST='localhost'
PORT=9090
message=[]

if len(sys.argv) == 2 or len(sys.argv) > 3:
	print(''' If you want to connect to a specific server you need to inform host and port.
Ex: python client.py localhost 9090 Or just run "$ python client.py" to use the default settings.''')
	exit()

if len(sys.argv) == 3:
	HOST = sys.argv[1]
	try:
		PORT = int(sys.argv[2])
	except ValueError:
		print('%s is a invalid value for port.' % sys.argv[2])
		exit()

def tryToUseMethodAnyServer(method, *args):

	try:
		ns = Pyro4.locateNS(host=HOST,port=PORT)
		server_names = ns.list('rmiserver-') #this should be returning me all servers registered on pyro's nameserver
		keys = list(server_names.keys())
	except Pyro4.errors.NamingError:
		print("\nFailed to locate the nameserver on %s:%d. Make sure it's running, execute: \n\npyro4-ns -n %s -p %d\n" % (HOST,PORT,HOST,PORT) )
		return False

	for key in keys:
		each_server = Pyro4.Proxy(server_names[key])

		try:
			return getattr(each_server, method)(*args)
		except Pyro4.errors.CommunicationError:
			pass
	
	print("Can't find any server available.")
	return False

while True:
	print ("#----------------------------------------------#")
	print ("#               MENU APP                       #")
	print ("# Options:                                     #")
	print ("# [1] multiply and find multiply is even or odd#")
	print ("# [0] Exit                                     #")
	print ("#----------------------------------------------#")

	try:
		option = input("Choose an option: ")
	except KeyboardInterrupt:
		print('\nThe connection was finished successfully...')
		break

	if option == "1":
		try:
			message1 = int(input("input 1st number: "))
			message.append(message1)
			message2= int(input("enter 2nd number: "))
			message.append(message2)
		except KeyboardInterrupt:
			print('\nThe connection was finished successfully...')
			break
		returnedMessage = tryToUseMethodAnyServer('echoService', message)
		if returnedMessage:
			print('multiply is: ', returnedMessage[0])
			if(returnedMessage[1]==0):
				print('multiply of the numbers is even')
				break
			else:
				print('multiply of the numbers is odd')
				break



	elif option == "0":
		print('The connection was finished successfully...')
		break
	else:
		print('Option not available.')
	
	input('Press Enter to continue...')