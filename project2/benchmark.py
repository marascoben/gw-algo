"""
This file is used to benchmark the performance of the algorithm under investigation. The date will be compared against the 
theoretical time complexity of the algorithm. 
"""
import time
from huffman import *
import random
import math


def generateTestCase(n):
    """
    Returns a tuple, containing a random list of length n containing symbols, and a random list of length n containing their 
    frequencies.
    """

    symbols = []
    frequencies = []

    for i in range(n):
        # A symbol can contain between 1 and 10 characters
        symbolLength = random.randint(1, 10)
        symbol = ""
        for j in range(symbolLength):
            # A character can be any letter from a-zA-Z
            symbol += chr(random.randint(97, 122))
        
        symbols.append(symbol)
        frequencies.append(random.randint(1, n))

    return (symbols, frequencies)

# Below are test cases of size 10, 100, 1000, 1000000, and 10000000

# Test case of size 10
symbols10, frequencies10 = generateTestCase(10)

# Test case of size 100
symbols100, frequencies100 = generateTestCase(100)

# Test case of size 1000
symbols1000, frequencies1000 = generateTestCase(1000)

# Test case of size 10000
symbols100000, frequencies100000 = generateTestCase(10000)

# Test case of size 100000
symbols100000, frequencies100000 = generateTestCase(100000)

# Test case of size 1000000
symbols1000000, frequencies1000000 = generateTestCase(1000000)


# Dictionary of test cases
testCases = {
    "10": (symbols10, frequencies10),
    "100": (symbols100, frequencies100),
    "1000": (symbols1000, frequencies1000),
    "10000": (symbols100000, frequencies100000),
    "100000": (symbols100000, frequencies100000),
    "1000000": (symbols1000000, frequencies1000000),
}

# Benchmark the algorithm
for key in testCases:
    symbols, frequencies = testCases[key]

    # Start the timer
    start = time.time()

    # Generate the huffman tree
    root = generateHuffmanTree(symbols, frequencies)

    # Stop the timer
    end = time.time()

    # Print the results in nanoseconds rounded to the nearest integer, in csv format
    duration = round((end - start) * 1000000000)
    print(key + "," + str(duration))
