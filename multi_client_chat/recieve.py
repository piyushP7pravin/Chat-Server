from threading import Thread
class Recieve(Thread):
	def __init__(self,skt):
		Thread.__init__(self)
		self.skt=skt
	def run(self):
		msg=""
		while msg!="bye":
			msg=self.skt.recv(1024).decode()
			print(msg)