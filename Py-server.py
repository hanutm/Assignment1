## ChartServer code using sockets

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 50000
server.bind((host.port))
server.listen(5)

chatroomname = {}
client = {}
while True:
	
	csock, addr = server.accept()

	#monitoring connections
	print("Connected to %s",str(addr))

	#processing response
	while True:
		conn_msg = csock.recv(1024)	#receiving 1024 bytes of data at a time (for testing)
		if not data: break
		
		#check incoming message
		print("Message received :", conn_msg
		
		#formatting incoming data
		rname_start = data.find('JOIN_CHATROOM')+3          #Chatroom Name
	 	rname_end = data.find('\n')-2
		chatroomname[0] = data[rname_start:rname_end]

		cname_start = data.find('CLIENT_NAME')+3	    #Client Name		
		cname_end = data.find('\n',cname_start)-2
		client[0] = data[cname_start:cname_end]
			
		#No other parameters to check because of TCP connection

	response = "Joined chatroom"
	csock.send(response.encode('ascii'))
	csock.close()

