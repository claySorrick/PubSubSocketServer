# -*- coding: utf-8 -*-
"""
Client- connect to server
		- publish or subscribe to topics

Created on Fri Jan 19 11:43:12 2018

@author: Clay Sorrick
"""
import socket

ADDRESS = "127.0.0.1"
PORT = 6000

print("CLIENT START")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Format:")
print("PUB/SUB:TOPIC:MESSAGE")
print("Topics: dog,cat,owl,bat")
msg = input()
pub_sub = msg[0:3].upper()
client_socket.connect((ADDRESS, PORT))
print("Sending message")
client_socket.send(bytes(msg, "utf-8"))
if pub_sub == "PUB": #publisher can publish messages
	while 1:
		print("Server:", msg)
		msg = input("PUB:TOPIC:MESSAGE or q\n")
		if msg == "q":
			client_socket.send(bytes(msg, "utf-8"))
			client_socket.close()
			print("closing socket and exiting")
			break;
		client_socket.send(bytes(msg, "utf-8"))
else: #subscriber just listens and prints new messages
	while 1:
		msg = client_socket.recv(512).decode()
		print("Server:", msg)
		if msg == "q":
			client_socket.close()
			print("Server closing socket and exiting")
			break;
