# -*- coding: utf-8 -*-
"""
Client- connect to server
		- publish or subscribe to topics

Created on Fri Jan 19 11:43:12 2018

@author: Clay Sorrick
"""
import socket

print("CLIENT START")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client_socket)