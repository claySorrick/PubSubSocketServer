Pub Sub Server

This is a publish/subscribe multi-thread socket server written in python 3.6

A server will hold a list of topics which clients may publish or subscribe to

A client can publish a message to one or more topics

A client can subscribe to one or more topics

The server will accept connections via a socket, determine if the message is a publish or subscribe, create a thread to handle the task

