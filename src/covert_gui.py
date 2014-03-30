#!/usr/bin/env python
import tkinter
import udp
import covertmsgr

class Covert_Gui(tkinter.Tk):
	
	udp_sender = None
	myhost_value = ""
	
	def __init__(self, parent):
		tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()
	
	def initialize(self):
		self.grid()
		cur_row = 0
		
		self.myhost_value = udp.UDP.host()
		myhost_label = tkinter.Label(self, anchor="e", text="This host:")
		myhost_label.grid(column=0, row=cur_row, sticky='EW')
		self.myhost_entry = tkinter.Entry(self, bg="#eeeeee")
		self.myhost_entry.grid(column=1, row=cur_row, sticky="EW")
		self.myhost_entry.insert(0, self.myhost_value)
		
		cur_row += 1
		host_label = tkinter.Label(self, anchor="e", text="Destination host:")
		host_label.grid(column=0, row=cur_row, sticky='EW')
		self.host_entry = tkinter.Entry(self, bg="#eeeeee")
		self.host_entry.grid(column=1, row=cur_row, sticky='EW')
		
		cur_row += 1
		port_label = tkinter.Label(self, anchor="e", text="Destination/Listening port:")
		port_label.grid(column=0, row=cur_row, sticky='EW')
		self.port_entry = tkinter.Entry(self, bg="#eeeeee")
		self.port_entry.grid(column=1, row=cur_row, sticky='EW')
		
		cur_row += 1
		filler1_label = tkinter.Label(self, anchor="w")
		filler1_label.grid(column=0, row=cur_row, sticky='EW')
		
		cur_row += 1
		covert_msg_label = tkinter.Label(self, anchor="w", text="Covert message:")
		covert_msg_label.grid(column=0, row=cur_row, sticky='EW')
		cur_row += 1
		self.covert_msg = tkinter.Text(self, height=5, relief="sunken", bg="#eeeeee")
		self.covert_msg.grid(column=0, row=cur_row, columnspan=2, sticky='EW')
		
		cur_row += 1
		filler2_label = tkinter.Label(self, anchor="w")
		filler2_label.grid(column=0, row=cur_row, sticky='EW')
		
		cur_row += 1
		plaintxt_msg_label = tkinter.Label(self, anchor="w", text="Plain text message:")
		plaintxt_msg_label.grid(column=0, row=cur_row, sticky='EW')
		cur_row += 1
		self.plaintxt_msg = tkinter.Text(self, height=5, relief="sunken", bg="#eeeeee")
		self.plaintxt_msg.grid(column=0, row=cur_row, columnspan=2, sticky='EW')
		
		cur_row += 1
		filler3_label = tkinter.Label(self, anchor="w")
		filler3_label.grid(column=0, row=cur_row, sticky='EW')
		
		cur_row += 1
		listen_button = tkinter.Button(self, text="Listen", command=self.listen)
		listen_button.grid(column=0, row=cur_row, sticky='EW')
		send_button = tkinter.Button(self, text="Send", command=self.send_message)
		send_button.grid(column=1, row=cur_row, sticky='EW')
		
		self.resizable(False, False)
	
	def send_message(self):
		covertmsgr.send_messasge(self.src_host(), self.host(), self.port(), self.covert_message(), self.plaintext_message())
	
	def listen(self):
		print("listening")
		covert_message, message = covertmsgr.receive_message(self.src_host(), self.port())
		self.set_covert_message(covert_message)
		self.set_plaintext_message(message)
	
	def src_host(self):
		return self.myhost_entry.get()
	
	def host(self):
		return self.host_entry.get()
	
	def port(self):
		return int(self.port_entry.get())
	
	def covert_message(self):
		return self.covert_msg.get(1.0, tkinter.END)
	
	def set_covert_message(self, string):
		self.covert_msg.insert(tkinter.END, string)
	
	def plaintext_message(self):
		return self.plaintxt_msg.get(1.0, tkinter.END)
	
	def set_plaintext_message(self, string):
		self.plaintxt_msg.insert(tkinter.END, string)
	
	
if __name__ == "__main__":
	app = Covert_Gui(None)
	app.title('Covert Messenger GUI')
	app.mainloop()