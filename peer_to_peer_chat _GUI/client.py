import socket
from send import *
from recieve import *
from DBConnection import DBconnection
import tkinter
from tkinter import messagebox

s=socket.socket()
s.connect(("localhost",12345))

class Login:
	def __init__(self):
		self.root=tkinter.Tk()
		self.root.title("FTP Server")
		self.root.geometry("350x150")
		tkinter.Label(self.root,text="Username").grid(row=0,column=0,padx=40,pady=20)
		tkinter.Label(self.root,text="Password").grid(row=1,column=0)
		self.username=tkinter.Entry(self.root)
		self.username.grid(row=0,column=1,pady=20)
		self.__password=tkinter.Entry(self.root,show="*")
		self.__password.grid(row=1,column=1)
		tkinter.Button(self.root,text="Login",command=self.btn_login_clicked).grid(row=3,columnspan=3,pady=20)
		self.__password.bind("<Return>",self.btn_login_clicked)
		tkinter.Button(self.root,text="Clear",command=self.btn_clear_clicked).grid(row=3,column=1)
		self.root.mainloop()
	def btn_login_clicked(self,event=None):
		uname=self.username.get()
		pd=self.__password.get()
		s.send(uname.encode())	
		s.send(pd.encode())
		if s.recv(1024).decode=="True":
			self.root.destroy()
			ChatWindow(un)
		else:
			messagebox.showerror("Error","Wrong username or password")
			self.root.destroy()
			Login()
	def btn_clear_clicked(self):
		self.__username.delete(0,"end")
		self.__password.delete(0,"end")
		
class ChatWindow:
	def __init__(self,un):
		
	
	
	
if __name__=="__main__":
	Login()

		
sd=Send(s)
r=Recieve(s)
sd.start()
r.start()
sd.join()
r.join()

s.close()