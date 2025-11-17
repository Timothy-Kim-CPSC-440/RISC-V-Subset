import unittest
from main import *

class TestNumOps(unittest.TestCase):
	#all asserted values were found using an online two's complement calculator
	def test_encode(self):
		print("Testing encode_twos_complement():\n -2^31")
		self.assertEqual(encode_twos_complement(-2**31)[0], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
		self.assertEqual(encode_twos_complement(-2**31)[1], "0x80000000")
		self.assertEqual(encode_twos_complement(-2**31)[2], 0)
		
		print(" -1")
		self.assertEqual(encode_twos_complement(-1)[0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
		self.assertEqual(encode_twos_complement(-1)[1], "0xFFFFFFFF")
		self.assertEqual(encode_twos_complement(-1)[2], 0)
		
		print(" -13")
		self.assertEqual(encode_twos_complement(-13)[0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1])
		self.assertEqual(encode_twos_complement(-13)[1], "0xFFFFFFF3")
		self.assertEqual(encode_twos_complement(-13)[2], 0)
		
		print(" -7")
		self.assertEqual(encode_twos_complement(-7)[0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1])
		self.assertEqual(encode_twos_complement(-7)[1], "0xFFFFFFF9")
		self.assertEqual(encode_twos_complement(-7)[2], 0)
		
		print(" 0")
		self.assertEqual(encode_twos_complement(0)[0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
		self.assertEqual(encode_twos_complement(0)[1], "0x00000000")
		self.assertEqual(encode_twos_complement(0)[2], 0)
		
		print(" 13")
		self.assertEqual(encode_twos_complement(13)[0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1])
		self.assertEqual(encode_twos_complement(13)[1], "0x0000000D")
		self.assertEqual(encode_twos_complement(13)[2], 0)
		
		print(" 2^31 - 1")
		self.assertEqual(encode_twos_complement(2**31 - 1)[0], [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
		self.assertEqual(encode_twos_complement(2**31 - 1)[1], "0x7FFFFFFF")
		self.assertEqual(encode_twos_complement(2**31 - 1)[2], 0)
		
		print(" -2^31 - 1")
		self.assertEqual(encode_twos_complement(-2**31 - 1)[0], [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
		self.assertEqual(encode_twos_complement(-2**31 - 1)[1], "0x7FFFFFFF")
		self.assertEqual(encode_twos_complement(-2**31 - 1)[2], 1)
		
		print(" 2^31")
		self.assertEqual(encode_twos_complement(2**31)[0], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
		self.assertEqual(encode_twos_complement(2**31)[1], "0x80000000")
		self.assertEqual(encode_twos_complement(2**31)[2], 1)
		
if __name__ == "__main__":
	unittest.main()
