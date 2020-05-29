from threading import Thread
class Broadcast(Thread):
	def __init__(self,skt,sktlist):
		Thread.__init__(self)
		self.skt=skt
		self.sktlist=sktlist
	def run(self):
		msg=""
		while True:
			msg=self.skt.recv(1024)
			for i in self.sktlist:
				i.send(msg)
				