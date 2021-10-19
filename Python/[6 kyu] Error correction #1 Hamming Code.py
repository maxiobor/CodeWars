# see https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e/train/python

# Good Luck!
def encode(string):
  binaries = [-len(bin(ord(letter))[2:]) % 8 * '0' + bin(ord(letter))[2:] for letter in string]
  retArray = []
  for binary in binaries:
    concatenate = "".join(str(digit)*3 for digit in binary)
    retArray.append(concatenate)
  return "".join(x for x in retArray)

def decode(bits):
  binaries = []
  pointer = 0
  while pointer + 2 < len(bits):
    binary = bits[pointer:pointer+3]
    countOne = binary.count('1')
    countZero = binary.count('0')
    binary = '1' if countOne > countZero else '0'
    binaries.append(binary)
    pointer += 3
  retArray = []
  pointer = 0
  while pointer + 7 < len(binaries):
    asciiValue = int("".join(x for x in binaries[pointer:pointer+8]), 2)
    byte_number = asciiValue.bit_length() + 7 // 8
    binary_array = asciiValue.to_bytes(byte_number, "big")
    asciiText = [x if x != "\x00" else "" for x in binary_array.decode()]
    retArray.append("".join(x for x in asciiText))
    pointer += 8
  return "".join(x for x in retArray)
    


from TestFunction import Test
test = Test(None)

# test.describe("Test encode function")
# test.it("Should work with short word")
# test.assert_equals(encode("hey"), "000111111000111000000000000111111000000111000111000111111111111000000111")
# test.it("Should work with long word")
# test.assert_equals(encode("The Sensei told me that i can do this kata"), "000111000111000111000000000111111000111000000000000111111000000111000111000000111000000000000000000111000111000000111111000111111000000111000111000111111000111111111000000111111111000000111111000111111000000111000111000111111000111000000111000000111000000000000000000111111111000111000000000111111000111111111111000111111000111111000000000111111000000111000000000000111000000000000000000111111000111111000111000111111000000111000111000000111000000000000000000111111111000111000000000111111000111000000000000111111000000000000111000111111111000111000000000000111000000000000000000111111000111000000111000000111000000000000000000111111000000000111111000111111000000000000111000111111000111111111000000000111000000000000000000111111000000111000000000111111000111111111111000000111000000000000000000111111111000111000000000111111000111000000000000111111000111000000111000111111111000000111111000000111000000000000000000111111000111000111111000111111000000000000111000111111111000111000000000111111000000000000111")
# test.it("Should work with numbers")
# test.assert_equals(encode("T3st"), "000111000111000111000000000000111111000000111111000111111111000000111111000111111111000111000000")
# test.it("Should work with special characters")
# test.assert_equals(encode("T?st!%"), "000111000111000111000000000000111111111111111111000111111111000000111111000111111111000111000000000000111000000000000111000000111000000111000111")

test.describe("Test decode function")
test.it("Should work with short word")
test.assert_equals(decode("100111111000111001000010000111111000000111001111000111110110111000010111"), "hey")
test.it("Should work with long word")
test.assert_equals(decode("000111000111000111000100000111111000111000001000000111111000010111000111000100111000000000000100000111000111000000111111000111111000000111000111000111111000111111111000000111111111000000111111000110111000000111000111000111111000111000000111000000111000000000000000000111111111000111000000000111111000111111111111000111111000111111000000000111111000000111000001000000111000000000001000000111111000111111000111000111111000000111000111000000111000000000000000000111111111000111000000000111111000111000000000000111111000000010000111000111111111000111000000000100111000000000000000000111111000111000000111000000111000000000000000000111111000000000111111000111111000000000000111000111111000111111111000000000111000000000000010000111111000000111000000000111111000111111110111000000111000000000000000000111111111000111000000000111111000111000000000000111111000111000000111000111111111000000111111000000111000000000000000000111111000111000111111000111111000000000000111000111111111000111000000000111111000000000000111"), "The Sensei told me that i can do this kata")
test.it("Should work with numbers")
test.assert_equals(decode("000111000111000111000010000000111111000000111111000111111111000000111111000111111111000111010000"), "T3st")
test.it("Should work with special characters")
test.assert_equals(decode("000111000111000111000001000000111111110111111111000111111111000000111111000111111111000111000000000000111000000000000111000000111000000111000111"), "T?st!%")
