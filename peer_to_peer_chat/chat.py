from threading import Thread

class Chat(Thread):
	def __init__(self,skt,user_skt):
		Thread.__init__(self)
		self.skt=skt
		self.user_skt=user_skt
	def run(self):
		msg=""
		username_chat=self.skt.recv(1024).decode()
		uc_skt=self.user_skt.get(username_chat)
		while True:
			msg=self.skt.recv(1024)
			uc_skt.send(msg)
				