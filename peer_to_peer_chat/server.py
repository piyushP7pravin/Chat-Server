import socket
from send import *
from recieve import *
from chat import *
from DBConnection import DBconnection

s=socket.socket()
s.bind(("",12345))
print("Socket server created")
s.listen(10)
print("waiting for client request")

def loginCheck(un,pd):
	result=False
	cnx=DBconnection.connect()
	cur=cnx.cursor()
	query="select username,password from user"
	cur.execute(query)
	d=cur.fetchall()
	for i in d:
		if i[0]==un and i[1]==pd:
			result=True
	cur.close()
	cnx.close()
	return result
	
user_skt={}
i=1

while i<=10:
	conn,addr=s.accept()
	print("connected to ",addr)
	while True:
		username=conn.recv(1024).decode()
		password=conn.recv(1024).decode()
		if loginCheck(username,password):
			conn.send("True".encode())
			user_skt[username]=conn
			break
		else:
			conn.send("False".encode())
	c=Chat(conn,user_skt)
	c.start()
	i+=1

conn.close()





