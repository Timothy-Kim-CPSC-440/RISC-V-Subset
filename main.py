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
	V, C, N, Z = 0, 0, 0, 1
	
	result = [0] * 32
	carry = 0
	
	for i in range(31, 0, -1):
		result[i] = num1[i] ^ num2[i]
		#print(f"bit {i}: num1 - {num1[i]} num2 - {num2[i]} carry - {carry} result - {result[i]}")
		
		if carry:
			result[i] = result[i] ^ 1
			#print("After 2nd XOR from carry:", result[i])
		
		#account for carryover into next iteration
		if (num1[i] & num2[i]) or (num1[i] & carry) or (num2[i] & carry):
			#condition: out of num1, num2, and carry, at least 2 of them are 1
			carry = 1
			
			#CARRY OUT
			if i == 0:
				C = carry
		
		else:
			carry = 0
			
		#ZERO: set to 1 by default, set to 0 if result is non-zero value
		if result[i]:
			Z = 0
	
	#NEGATIVE
	N = result[0]
	
	#SIGNED OVERFLOW
	V = (~(num1[0] ^ num2[0])) & (result[0] ^ num1[0])
	
	return result, V, C, N, Z

# -------------- DEBUGGING/TESTS -------------- #
#if __name__ == "__main__":
#	test1 = 13
#	test2 = 7
#	print("Binary bits:", encode_twos_complement(test1)[0])
#	print("Hex string:", encode_twos_complement(test1)[1])
#	print("Overflow:", encode_twos_complement(test1)[2])

#	test1 = encode_twos_complement(test1)[0]
#	test2 = encode_twos_complement(test2)[0]

#	for i in range(0, 5):
#		print(int_add(test1, test2)[i])
