import socket
import string

EOF = "####EOF####"

class UDP:
	udp_socket = None
	
	destination_host = ""
	destination_port = 0
	
	def __init__(self, destination_host, destination_port):
		self.destination_host = destination_host
		self.destination_port = destination_port
	
	def send(self, source_host, source_port, data):
		#debug print "src_host: " + source_host + ", src_port: " + str(source_port)
		self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.udp_socket.bind((source_host, source_port))
		self.udp_socket.sendto(data.encode('utf-8'), (self.destination_host, self.destination_port))
	
	@staticmethod
	def host():
		return socket.gethostbyname(socket.gethostname())
	
	def receive(self):
		self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.udp_socket.bind((self.destination_host, self.destination_port))
		
		encoded_values = []
		message = ""
		
		# read from port until EOF identifier is reached
		eof_reached = False
		while not eof_reached:
			#debug print("receiving...")
			data, address = self.udp_socket.recvfrom(1024)
			str_data = str(data, encoding='utf-8')
			if EOF in str_data: eof_reached = True
			encoded_values.append(address[1])
			message += str_data
			#debug print("received: ", str_data, ", port: ", address[1])
		
		# remove the EOF identifier from the message
		message = message[0:message.find(EOF)]
		
		return encoded_values, message
	
