import socket
import os
s=socket.socket()
s.connect(("localhost",12345))

while True:
	un=input('Enter username :')
	s.send(un.encode())
	un_check=s.recv(1024).decode()
	pd=input('Enter password :')
	s.send(pd.encode())
	pd_check=s.recv(1024).decode()
	if un_check=='True' and pd_check=='True':
		s.send('True'.encode())
		break
	else:
		print('Invalid username or password. Try again.')
		s.send('False'.encode())
print(s.recv(1024).decode())		

while True:
	print()
	print("1. Chat")
	print("2. View chat history")
	print("3. Download file")
	print("4. Upload file")
	print("5. Exit")
	choice=int(input("Enter your choice : "))
	if choice==1:
		s.send(str(choice).encode())
		msg=''
		while True:
			msg=input('Enter message :')
			s.send(msg.encode())
			msg=s.recv(1024).decode()
			print(msg)
	elif choice==2:
		s.send(str(choice).encode())
		if s.recv(1024).decode()=="True":
			chat=s.recv(1024).decode()
			while chat:
				print(chat,end="")
				chat=s.recv(1024).decode()
			print("chat viewed")
		else:
			print("No chat history")
	elif choice==3:
		s.send(str(choice).encode())
		filename=input("Enter filename : ")
		s.send(filename.encode())
		if s.recv(1024).decode()=="True":
			print("Download begins")
			f=open(filename,"wb")
			data=s.recv(4096)
			while data:
				f.write(data)
				data=s.recv(4096)
			f.close()
			print("Downloading finished")
		else:
			print("File not found")
	elif choice==4:
		s.send(str(choice).encode())
		filepath=input("Enter file path : ")
		filename=filepath.split("\\")[-1]
		if os.path.exists(filepath):
			s.send("True".encode())
			s.send(filename.encode())
			print("Uploading begins")
			f=open(filepath,"rb")
			data=f.read(4096)
			while data:
				s.send(data)
				data=f.read(4096)
			s.shutdown(socket.SHUT_RDWR)
			print("File uploaded")
			f.close()
		else:
			print("File not found")	
	elif choice==5:
		s.send(str(choice).encode())
		print("Thank You")
		break
	else:
		s.send(str(choice).encode())
		print("Wrong choice")		
s.close()
			