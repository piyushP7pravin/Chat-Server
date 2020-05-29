import socket
from send import *
from recieve import *
from broadcast import *
s=socket.socket()
s.bind(("",12345))
print("Socket server created")
s.listen(10)
print("waiting for client request")

sktlist=[]
i=1
while i<=10:
	conn,addr=s.accept()
	sktlist.append(conn)
	print("connected to ",addr)
	b=Broadcast(conn,sktlist)
	b.start()
	i+=1

conn.close()