import socket
from send import *
from recieve import *
from DBConnection import DBconnection

s=socket.socket()
s.connect(("localhost",12345))


while True:
	username=input('Enter username :')
	password=input('Enter password :')
	s.send(username.encode())	
	s.send(password.encode())	
	if s.recv(1024).decode()=="True":
		print("Login Success")
		break
	else:
		print('Invalid username or password. Try again.')
username_chat=input("Enter username to chat with : ")
s.send(username_chat.encode())
		
sd=Send(s)
r=Recieve(s)
sd.start()
r.start()
sd.join()
r.join()

s.close()