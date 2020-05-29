import socket
from send import *
from recieve import *

s=socket.socket()
s.connect(("localhost",12345))

sd=Send(s)
r=Recieve(s)
sd.start()
r.start()
sd.join()
r.join()

s.close()