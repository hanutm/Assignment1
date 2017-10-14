## ChartServer code using sockets

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 50000
server.bind((host,port))
server.listen(0)
print(host)
chatroomname = {}
client = {}
while True:
	
	csock, addr = server.accept()

	#monitoring connections
	print("Connected to %s",str(addr))

	#processing response
	while True:
		conn_msg = csock.recv(1024)	#receiving 1024 bytes of data at a time (for testing)
		if not conn_msg: break
		
		#check incoming message
		print("Message received :", conn_msg)
		
		#formatting incoming data
		rname_start = conn_msg.find("JOIN_CHATROOM".encode(encoding='utf-8')) + 3          #Chatroom Name
		rname_end = conn_msg.find(b'\n') - 2
		chatroomname[0] = conn_msg[rname_start:rname_end]

		cname_start = conn_msg.find("CLIENT_NAME".encode(encoding='utf-8'))+3	    #Client Name		
		cname_end = conn_msg.find(b'\n',cname_start)-2
		client[0] = conn_msg[cname_start:cname_end]
			
		#No other parameters to check because of TCP connection

		response = "Joined chatroom"
		csock.send(response.encode('ascii'))
		csock.close()
		break
	break
