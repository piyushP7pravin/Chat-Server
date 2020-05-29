import socket
import datetime
import os
s=socket.socket()
s.bind(("",12345))
print("Socket server created")
s.listen(1)
print("Waiting for client request")
conn,addr=s.accept()
print("Connected to ",addr)

u1="admin"
p1="admin"
while True:
	un=conn.recv(1024).decode()
	if un==u1:
		conn.send('True'.encode())
	else:
		conn.send('False'.encode())
	pd=conn.recv(1024).decode()
	if pd==p1:
		conn.send('True'.encode())
	else:
		conn.send('False'.encode())
	check=conn.recv(1024).decode()
	if check=='True':
		conn.send("Username-Password matched".encode())
		break
		
while True:
	choice=int(conn.recv(1024).decode())
	if choice==1:
		f=open("chat_history.txt","a")
		msg=''
		while True:
			msg=conn.recv(1024).decode()
			f.write(str(datetime.datetime.date(datetime.datetime.now()))+" "+str(datetime.datetime.now().strftime("%H:%M:%S"))+" Client : "+msg+"\n")
			print(msg)
			msg=input('Enter message :')
			f.write(str(datetime.datetime.date(datetime.datetime.now()))+" "+str(datetime.datetime.now().strftime("%H:%M:%S"))+" Server : "+msg+"\n")
			conn.send(msg.encode())
		f.close()	
	elif choice==2:
		if os.path.exists("chat_history.txt"):
			conn.send("True".encode())
			f=open("chat_history.txt","r")
			chat=f.read(1024)
			while chat:
				conn.send(chat.encode())
				chat=f.read(1024)
			print("Chat history sent")
			f.close()
		else:
			conn.send("False".encode())
	elif choice==3:
		filename=conn.recv(1024).decode()
		if os.path.exists(filename):
			conn.send("True".encode())
			f=open(filename,"rb")
			data=f.read(4096)
			while data:
				conn.send(data)
				data=f.read(4096)
			print("File sent")
			socket.SHUT_RDWR
			f.close()
		else:
			conn.send("False".encode())
	elif choice==4:
		if conn.recv(1024).decode()=="True":
			filename=conn.recv(1024).decode()
			f=open(filename,"wb")
			data=conn.recv(4096)              
			while data:
				f.write(data)
				data=conn.recv(4096)
			print("File recieved")
			f.close()		
	elif choice==5:
		break
	else:
		pass	
conn.close()
	
	
	
	
	