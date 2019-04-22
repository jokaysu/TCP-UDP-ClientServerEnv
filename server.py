import sys

from socket import *

if len(sys.argv) != 2:
	print 'Usage: ./server.sh <req_code>'
	sys.exit()

#negotiation stage
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 0))
addr = serverSocket.getsockname()
print 'SERVER_PORT=', addr[1]
while True:
	serverSocket.listen(1)
	connectionSocket, tcpaddr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	if sentence == sys.argv[1]:
		#transaction stage
		actualSocket = socket(AF_INET, SOCK_DGRAM)
		actualSocket.bind(('',0))
		connectionSocket.send(str(actualSocket.getsockname()[1]).encode())
		message, clientAddress = actualSocket.recvfrom(2048)
		reversedMessage = message[::-1]
		actualSocket.sendto(reversedMessage.encode(), clientAddress)
	else:
		connectionSocket.close()
		serverSocket.close()
		break
