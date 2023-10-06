from huffman import *

# Below is a test case to verify that this implementation is working as expected, this was sourced from
# https://en.wikipedia.org/wiki/Huffman_coding#Example
testString = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
expectedString = "1000011101001000110010011101100111001001000111110010011111011111100010001111110100111001001011111011101000111111001"

symbols, frequencies = parseString(testString)
root = generateHuffmanTree(symbols, frequencies)
codes = generateHuffmanCodes(root)


encodedString = encodeString(testString, codes)
print("Encoded string: " + encodedString)

decodedString = decodeString(encodedString, root)
print("Decoded string: " + decodedString)

assert decodedString == testString, "Decoded string does not match original string"

