def encode_twos_complement(base10: int):
	binary = [0] * 32
	hexa = "0x"
	overflow = 0
	
	# --- OVERFLOW --- #
	if base10 not in range((-2)**31, 2**31):
		overflow = 1
		
	# --- BINARY --- #
	neg = False		#flag for negative int
	if base10 < 0:
		neg = True
		base10 *= -1
	
	#convert to bit vector
	for i in range(31, -1, -1):		#accounts for positive overflow
		binary[i] = base10 % 2
		base10 = int(base10 / 2)
	
	#apply twos complement to negative int
	if neg:
		#bit flip (~)
		for i in range(31, -1, -1):
			binary[i] = (binary[i] + 1) % 2
		
		#carryover (+1)
		binary[31] = (binary[31] + 1) % 2
		if binary[31] == 0:
			i = 30
			
			#chain carryovers
			while i > -1 and binary[i] == 1:
				binary[i] = (binary[i] + 1) % 2
				i -= 1

			#atp the final carryover recepient is a 0
			binary[i] = (binary[i] + 1) % 2
				
	# --- HEX --- #
	x = 0		#value of each hex digit in base-10
	for i in range(0, 32):	
		x += binary[i] * (2 ** (3 - (i % 4)))
		
		#append hex digit
		if ((i + 1) % 4) == 0:
			match x:
				case 15:
					hexa += "F"
				case 14:
					hexa += "E"
				case 13:
					hexa += "D"
				case 12:
					hexa += "C"
				case 11:
					hexa += "B"
				case 10:
					hexa += "A"
				case _:
					hexa += str(x)
			
			x = 0
	
	return [binary, hexa, overflow]

def int_add(num1: [], num2: []):
	#ALU flags
	V, C, N, Z = 0
	
	result = [0] * 32
	carry = False
	
	for i in range(31, 0, -1):
		result[i] = num1[i] ^ num2[i]
		if carry:
			result[i] = result[i] ^ 1
		
		if num1[i] & num2[i]:
			carry = True

if __name__ == "__main__":
	test = -2**31
	print("Binary bits:", encode_twos_complement(test)[0])
	print("Hex string:", encode_twos_complement(test)[1])
	print("Overflow:", encode_twos_complement(test)[2])
