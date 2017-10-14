## ChartServer code using sockets

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 50000

server.bind((host.port))

server.listen(5)

while True:
	
	csock, addr = server.accept()
	
	print("Connected with %s" % str(addr))

	response = "Joined chatroom"
	csock.send(response.encode('ascii'))
	csock.close()

