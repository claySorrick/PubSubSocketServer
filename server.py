# -*- coding: utf-8 -*-
"""
Server- listen for connections
		- hold subscriber connections
		- publish publisher messages
		
Created on Fri Jan 19 11:43:15 2018

@author: Clay Sorrick
"""
import socket

print("SERVER START")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server_socket)