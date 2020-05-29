import socket
from send import *
from recieve import *

s=socket.socket()
s.bind(("",12345))
print("Socket server created")
s.listen(1)
print("waiting for client request")
conn,addr=s.accept()
print("connected to ",addr)

sd=Send(conn)
r=Recieve(conn)
sd.start()
r.start()
sd.join()
r.join()

conn.close()