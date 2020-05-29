from threading import Thread
class Send(Thread):
	def __init__(self,skt):
		Thread.__init__(self)
		self.skt=skt
		
	def run(self):
		msg=""
		while msg!="bye":
			msg=input()
			self.skt.send(msg.encode())
			