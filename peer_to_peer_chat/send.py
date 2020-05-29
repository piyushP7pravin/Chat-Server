from threading import Thread
class Send(Thread):
	def __init__(self,skt):
		Thread.__init__(self)
		self.skt=skt
		
	def run(self):
		msg=""
		while True:
			msg=input()
			self.skt.send(msg.encode())
			