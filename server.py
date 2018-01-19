# -*- coding: utf-8 -*-
"""
Server- listen for connections
		- hold subscriber connections
		- publish publisher messages
		
Created on Fri Jan 19 11:43:15 2018

@author: Clay Sorrick
"""
import socket, threading

class Topic:
	def __init__(self, name):
		self.name = name
		self.messages = []
		self.subscribers = dict([])
		
	def add_subscriber(self, subscriber):
		if subscriber not in self.subscribers:
			self.subscribers[subscriber] = 0
			self.send_messages()
		
	def add_message(self, message):
		self.messages.append(message)
		self.send_messages()
		
	def send_messages(self):
		for sub in self.subscribers:
			index = self.subscribers[sub]
			for a in range(index, len(self.messages)):
				msg = "SUB:" + self.name + ":" + self.messages[a]
				sub.send_message(msg)
			self.subscribers[sub] = len(self.messages)

class ThreadManager:
	
	def __init__(self, thread_max):
		self.thread_max = thread_max
		self.threads = []
		self.topics_list = dict([])

	def new_thread(self, address, c_socket):
		msg = c_socket.recv(512).decode()
		if len(self.threads) >= self.thread_max:
			for thread in self.threads:
				thread.stop()
			return -1
		else:
			pub_sub = msg[0:3]
			topicChunk = msg[4:msg.index(":", 4)]
			topics = topicChunk.split(",")
			msg = msg[msg.index(":", 4) + 1:]
			thread = self.ClientThread(address, c_socket)
			if pub_sub == "PUB":
				for topic in topics:
					if topic in self.topics_list:
						self.topics_list[topic].add_message(msg)
				print("\nClient: %s" % msg)
				thread.add_topics_list(self.topics_list)
				thread.start()
			elif pub_sub == "SUB":
				for topic in topics:
					if topic in self.topics_list:
						self.topics_list[topic].add_subscriber(thread)
			self.threads.append(thread)
			print("Threads:", self.threads)
		

	#a client thread to hold subscriber connection or write publisher message
	class ClientThread(threading.Thread):
		def __init__(self, client_address, client_socket):
			threading.Thread.__init__(self)
			self.c_socket = client_socket
			self.c_addr = client_address
			self.topics_list = dict([])
			print("New thread on new connection:", self.c_addr)
		
		def run(self):
			while 1:
				data = self.c_socket.recv(512)
				msg = data.decode()
				print("\nClient: %s" % msg)
				if msg == "q":
					print("Client closed socket")
					client_socket.close()
					break;
				topicChunk = msg[4:msg.index(":", 4)]
				topics = topicChunk.split(",")
				msg = msg[msg.index(":", 4) + 1:]
				for topic in topics:
					if topic in self.topics_list:
						self.topics_list[topic].add_message(msg)
						
		def stop(self):
			self.c_socket.send(bytes("q","utf-8"))
			print("closing client socket")
			self.c_socket.close()
			
		def add_topics_list(self, topics_list):
			self.topics_list = topics_list
		
		def send_message(self, msg):
			print("Sending message on thread {}\n on connection: {}".format(
					self, self.c_addr))
			self.c_socket.send(bytes(msg, "utf-8"))
			
	
ADDRESS = "127.0.0.1"
PORT = 6000

THREAD_MAX = 4
#create thread manager to create new threads for new client connections
t_man = ThreadManager(THREAD_MAX)
#create defalt Topics
dog = Topic("dog")
cat = Topic("cat")
owl = Topic("owl")
bat = Topic("bat")
#add Topics to thread managers topic list
t_man.topics_list["dog"] = dog
t_man.topics_list["cat"] = cat
t_man.topics_list["owl"] = owl
t_man.topics_list["bat"] = bat

print("SERVER START")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ADDRESS,PORT))
server_socket.listen(5)
print("Server is listening on %s:%d" % (ADDRESS,PORT))
while 1:
	client_socket, address = server_socket.accept()
	if t_man.new_thread(address,client_socket) == -1:
		print("exiting")
		exit()
	
		
	
	
