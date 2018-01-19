# -*- coding: utf-8 -*-
"""
Server- listen for connections
		- hold subscriber connections
		- publish publisher messages
		
Created on Fri Jan 19 11:43:15 2018

@author: Clay Sorrick
"""
import socket, threading

class ThreadManager:
	
	def __init__(self, thread_max):
		self.thread_max = thread_max
		self.threads = []

	def new_thread(self, address, c_socket):
		thread = self.ClientThread(address, c_socket)
		c_socket.send(bytes("connected", "utf-8"))
		thread.start()
		self.threads.append(thread)
		

	#a client thread to hold subscriber connection or write publisher message
	class ClientThread(threading.Thread):
		def __init__(self, client_address, client_socket):
			threading.Thread.__init__(self)
			self.c_socket = client_socket
			self.c_addr = client_address
			print("New thread on new connection:", self.c_addr)
		
		def run(self):
			print("running")
			while 1:
				data = self.c_socket.recv(512)
				msg = data.decode()
				print("Client: %s" % msg)
				if msg == "q":
					print("Client closed socket")
					client_socket.close()
					break;
				self.c_socket.send(data)
			
	
ADDRESS = "127.0.0.1"
PORT = 6000

THREAD_MAX = 4
#create thread manager to create new threads for new client connections
t_man = ThreadManager(THREAD_MAX)

print("SERVER START")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server_socket)
server_socket.bind((ADDRESS,PORT))
print(server_socket)
server_socket.listen(5)
print("Server is listening on %s:%d" % (ADDRESS,PORT))
while 1:
	client_socket, address = server_socket.accept()
	t_man.new_thread(address,client_socket)
	
		
	
	
