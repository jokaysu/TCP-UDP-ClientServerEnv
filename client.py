import sys

from socket import *

if len(sys.argv) != 5:
	print 'Usage: ./client.sh <server_address> <n_port> <req_code> <msg>'
	sys.exit()

#negotiation stage
clientSocket = socket(AF_INET, SOCK_STREAM)
#print 'Trying to connect ', sys.argv[1], ' port: ', int(sys.argv[2]) 
clientSocket.connect((sys.argv[1], int(sys.argv[2])))
clientSocket.send(sys.argv[3].encode())
rPort = clientSocket.recv(1024).decode()
clientSocket.close()

#transaction stage
actualSocket = socket(AF_INET, SOCK_DGRAM)
actualSocket.sendto(sys.argv[4].encode(), (sys.argv[1], int(rPort)))
reversedMessage, serverAddress = actualSocket.recvfrom(2048)
print (reversedMessage.decode())
actualSocket.close()
