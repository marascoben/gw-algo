# Benjamin Marasco
# 10-06-2023
# CSCI 6212 - Project 2

import heapq

# Node class for Huffman tree
class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    # Overload comparison operators
    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq

def generateHuffmanTree(symbols, frequencies):
    """
    Generates a Huffman tree from a list of symbols and their frequencies, then returns the root node.
    """
    pqueue = []

    # Create nodes representing each symbol, then add to the priority queue, then heapify.
    # This operation is O(n) for node creation, and O(len(heap)) aka O(n) for heapify, so
    # the total operation is O(n) + O(n) = O(n)
    for i in range(len(symbols)):
        pqueue.append(Node(symbols[i], frequencies[i]))
    heapq.heapify(pqueue)

    # Create the huffman tree by popping the two lowest frequency nodes, then creating a new parent node
    # with the sum of the two frequencies. Then, add the two nodes as children of the parent node, and
    # add the parent node back into the priority queue. This operation is O(n) for the while loop, and
    # O(log(n)) for each heap push and pop, so the total operation is O(n * log(n))
    while len(pqueue) > 1:
        left = heapq.heappop(pqueue)
        right = heapq.heappop(pqueue)

        # Generate the new parent node
        parent = Node(None, left.freq + right.freq)

        parent.left = left
        parent.right = right
        heapq.heappush(pqueue, parent)

    # Return the root node of the huffman tree
    return heapq.heappop(pqueue)

def generateHuffmanCodes(root):
    """
    Generates a dictionary of symbols and their huffman codes from a huffman tree.
    """
    codes = {}

    def generateHuffmanCodesHelper(root, code):
        """
        Helper function for generating huffman codes. Recursively traverses the huffman tree and
        generates the huffman codes for each symbol.
        """
        if root == None:
            return
        if root.symbol != None:
            codes[root.symbol] = code
        generateHuffmanCodesHelper(root.left, code + '0')
        generateHuffmanCodesHelper(root.right, code + '1')

    generateHuffmanCodesHelper(root, '')
    return codes

def encodeString(string, codes):
    """
    Encodes a string using a dictionary of huffman codes.
    """
    encodedString = ''
    for char in string:
        encodedString += codes[char]
    return encodedString

def decodeString(string, root):
    """
    Decodes a string using a huffman tree.
    """

    decodedString = ''
    currentNode = root
    for bit in string:
        if bit == '0':
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
        if currentNode.symbol != None:
            decodedString += currentNode.symbol
            currentNode = root
    return decodedString

def parseString(string):
    """
    Parses a string and returnes a tuple containing symbols and their frequencies.
    """
    symbols = []
    frequencies = []
    for char in string:
        if char not in symbols:
            symbols.append(char)
            frequencies.append(1)
        else:
            frequencies[symbols.index(char)] += 1
    return (symbols, frequencies)
