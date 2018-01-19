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
print(client_socket)
client_socket.connect((ADDRESS, PORT))
print(client_socket)
client_socket.send(bytes("HELLO", "utf-8"))
print("Establishing connection...")

while 1:
	msg = client_socket.recv(512).decode()
	if msg == "q":
		print("server closed socket")
		client_socket.close()
		break;
	print("Server: %s" % msg)
	print("REPLY")
	msg = input()
	if msg == "q":
		client_socket.send(bytes(msg, "utf-8"))
		client_socket.close()
		print("closing socket and exiting")
		break;
	client_socket.send(bytes(msg, "utf-8"))