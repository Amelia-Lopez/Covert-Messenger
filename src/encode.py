import random
import string

# we can fit 3 characters (40 unique possibilities) within 65k values
STRING_SEGMENT_LENGTH = 3

# end of file
EOF = 'e'

# Python used 0-based arrays
FIRST_POS = 0

ENCODING = {
	EOF: 0,
	'A': 1,
	'B': 2,
	'C': 3,
	'D': 4,
	'E': 5,
	'F': 6,
	'G': 7,
	'H': 8,
	'I': 9,
	'J': 10,
	'K': 11,
	'L': 12,
	'M': 13,
	'N': 14,
	'O': 15,
	'P': 16,
	'Q': 17,
	'R': 18,
	'S': 19,
	'T': 20,
	'U': 21,
	'V': 22,
	'W': 23,
	'X': 24,
	'Y': 25,
	'Z': 26,
	'0': 27,
	'1': 28,
	'2': 29,
	'3': 30,
	'4': 31,
	'5': 32,
	'6': 33,
	'7': 34,
	'8': 35,
	'9': 36,
	' ': 37,
	'.': 38,
	'?': 39
}

DECODING = {v:k for k, v in ENCODING.items()}

'''
Encodes a string into grouped numerical values and padded with random values
For example:
Message: AbcDEF []
Characters are made upper-case: ABCDEF []
Characters converted to values and invalid characters dropped: 1, 2, 3, 4, 5, 37
End of file symbol appended: 1, 2, 3, 4, 5, 37, 40
Random values appended: 1, 2, 3, 4, 5, 37, 40, 3
Values are groupped together: 4881, 9804, 6437
'''
def encode(string):
	string = string.upper()
	#debug print "string: [" + string + "]"
	single_encoded_values = []
	grouped_encoded_values = []
	
	# encode each valid character
	for char in string:
		encoded_value = get_value_for_char(char)
		if encoded_value != None:
			single_encoded_values.append(encoded_value)
	#debug print "encoded values: " + str(single_encoded_values)
	
	# add EOF to the list
	single_encoded_values.append(get_value_for_char(EOF))
	#debug print "encoded values: " + str(single_encoded_values)
	
	# pad values to be divisble by STRING_SEGMENT_LENGTH
	while (len(single_encoded_values) % STRING_SEGMENT_LENGTH != 0):
		# pad with random values after EOF to decrease predictability
		single_encoded_values.append(random.randint(1, len(ENCODING)))
	#debug print "encoded values: " + str(single_encoded_values)
	
	# group values in segments of STRING_SEGMENT_LENGTH and calculate unique values
	while (len(single_encoded_values) > 0):
		# create a group of the specified segment length
		group_value = 0
		for x in range(0, STRING_SEGMENT_LENGTH):
			# ABC => 1,2,3 => (1 * 40^0) + (2 * 40^1) + (3 * 40^2) = 4881
			group_value += single_encoded_values.pop(FIRST_POS) * (len(ENCODING) ** x)
		grouped_encoded_values.append(group_value)
	#debug print "encoded grouped values: " + str(grouped_encoded_values)
	
	return grouped_encoded_values

def get_value_for_char(char):
	# pull character from ENCODING map, default to removing the character from the message
	return ENCODING.get(char, None)

def get_char_for_value(char):
	return DECODING.get(char, '#')

def decode(group_values):
	decoded_string = ""
	eof_reached = False
	
	# go through each group value
	for group_value in group_values:
		if eof_reached:
			break
		
		# convert each value into a character
		decoded_group = ""
		for x in range(STRING_SEGMENT_LENGTH-1, -1, -1):
			value = int(group_value / (len(ENCODING) ** x))
			#debug print("value: ", str(value))
			group_value = group_value % (len(ENCODING) ** x)
			#debug print("new group value: ", group_value)
			char = get_char_for_value(value)
			if (char == EOF):
				eof_reached = True
			decoded_group = char + decoded_group
		
		decoded_string += decoded_group
	
	# remove the EOF and everything after it
	decoded_string = decoded_string[0:decoded_string.find(EOF)]
	
	return decoded_string






