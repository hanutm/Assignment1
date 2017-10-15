## ChartServer code using sockets

import socket
from threading import Thread

def check_msg(msg):
	if (msg.find('JOIN_CHATROOM'.encode('utf-8'))+1):
		return(1)	
	elif (msg.find('LEAVE_CHATROOM'.encode('utf-8'))+1):
		return(2)
	elif (msg.find('DISCONNECT'.encode('utf-8'))+1):
		return(3)
	elif (msg.find('CHAT:'.encode('utf-8'))+1):
		return(4)	
	else:
		return(5)

def join(conn_msg):
	gname = conn_msg.find(':'.encode('utf-8'))+2
	gname_end = conn_msg.find('\n'.encode('utf-8'))-1
	groupname = conn_msg[gname:gname_end]
	cname = conn_msg.find('CLIENT_NAME'.encode('utf-8'))+13
	cname_end = conn_msg.find(' '.encode('utf-8'),cname)
	clientname = conn_msg[cname:cname_end]
	return groupname,clientname

#def leave():
#	print(clThread.ip)
#	print(clThread.port)
#	print(clThread.roomname)
#	print(clThread.clientid)

class client_threads(Thread):

	def __init__(self,ip,port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port

	def run(self):
		while True:
			conn_msg = csock.recv(1024)
			cflag = check_msg(conn_msg)	
#			print(conn_msg)
			if cflag == 1 : self.roomname,self.clientid = join(conn_msg)
			elif cflag == 2 : leave()
			elif cflag == 3 : discon()
			elif cflag == 4 : chat()
			else : pass #error code for incorrect message	
#			leave()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 50000
server.bind((host,port))
print(host)
thread_count = [] 
while True:
	server.listen(4)
	(csock,(ip,port)) = server.accept()

	print("Connected to ",port,ip)
	#monitoring connections

	clThread = client_threads(ip,port)
	clThread.start()
	thread_count.append(clThread)
