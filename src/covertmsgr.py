import encode
import udp
import random

SOURCE_PORT_MIN_INT = 2**10 + 1
SOURCE_PORT_MAX_INT = 2**16 - 1

def send_messasge(src_host, host, port, covert_msg, plaintext_msg):
	plaintext_msg += udp.EOF
	encoded_input = encode.encode(covert_msg)
	#debug print "encoded input: " + str(encoded_input)
	packet_sender = udp.UDP(host, port)
	msg_length = len(plaintext_msg)
	msg_segment_size = msg_length / len(encoded_input) + 1
	
	min = 0
	max = int(msg_length / msg_segment_size) + 1
	for x in range(min, max):
		# determine what part of the fake message to send in this packet
		start = int(x * msg_segment_size)
		end = int(start + msg_segment_size)
		if end > msg_length:
			end = msg_length

		# determine what should be sent for the covert message
		covert_msg_segment = 0
		if x < len(encoded_input):
			covert_msg_segment = encoded_input[x]
		else:
			covert_msg_segment = random.randint(SOURCE_PORT_MIN_INT, SOURCE_PORT_MAX_INT)

		packet_sender.send(src_host, covert_msg_segment, plaintext_msg[start:end])
	
	
def receive_message(host, port):
	packet_receiver = udp.UDP(host, port)
	encoded_values, message = packet_receiver.receive()
	
	covert_message = encode.decode(encoded_values)
	return covert_message, message
	
