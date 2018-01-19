# -*- coding: utf-8 -*-
"""
Server- listen for connections
		- hold subscriber connections
		- publish publisher messages
		
Created on Fri Jan 19 11:43:15 2018

@author: Clay Sorrick
"""
import socket

ADDRESS = "127.0.0.1"
PORT = 6000

print("SERVER START")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server_socket)
server_socket.bind((ADDRESS,PORT))
print(server_socket)
server_socket.listen(5)
print("Server is listening on %s:%d" % (ADDRESS,PORT))


client_socket = server_socket.accept()
print(client_socket)
