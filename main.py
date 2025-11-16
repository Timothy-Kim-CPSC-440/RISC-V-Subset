def encode_twos_complement(base10: int):
	binary = [0] * 32
	hexa = "0x"
	overflow = 0
	
	# --- OVERFLOW --- #
	if base10 > (2**31 - 1):
		overflow = 1
		
	# --- BINARY --- #
	neg = False		#flag for negative int
	if base10 < 0:
		neg = True
		binary[0] = 1
		base10 *= -1
	
	#convert to bit vector
	for i in range(31, 0, -1):
		binary[i] = base10 % 2
		base10 = int(base10 / 2)
	
	#apply twos complement to negative int
	if neg:
		#bit flip (~)
		for i in range(31, 0, -1):
			binary[i] = (binary[i] + 1) % 2
		
		#carryover (+1)
		binary[31] = (binary[31] + 1) % 2
		if binary[31] == 0:
			i = 30
			while binary[i] == 1:
				binary[i] = 0
				i -= 1
				
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

test = 21197974919
print("Binary bits:", encode_twos_complement(test)[0])
print("Hex string:", encode_twos_complement(test)[1])
print("Overflow:", encode_twos_complement(test)[2])
