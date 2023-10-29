from solution import *
from numpy import random

# Testing the result of partition in solution.py
def testingPartition():
    # Test #1: No equal sum
    arr = [100, 150, 100, 50, 102, 259]
    result1 = partition(arr)

    if result1 == None:
        print("Test #1: CORRECT")
    else:
        print("Test #1: INCORRECT")

    # Test #2: Equal sum
    arr = [100, 100]
    result2 = partition(arr)

    if len(result2[0]) == 1 and len(result2[0]) == 1:
        if result2[0][0] == 100 and result2[1][0] == 100:
            print("Test #2: CORRECT")
        else:
            print("Test #2: INCORRECT")
    else:
        print("TEST #2: INCORRECT")

    # Test #3: Equal sum with larger array
    arr = [100, 100, 593, 501, 591, 591, 593, 501, 200]
    result3 = partition(arr)
    
    verifyFlag = True
    arr1 = [100, 100, 593, 501, 591]
    arr2 = [591, 593, 501, 200]
    if len(result3[0]) == 5 and len(result3[1]) == 4:
        for i in range(len(result3[0])):
            if result3[0][i] != arr1[i]:
                verifyFlag = False

        for i in range(len(result3[1])):
            if result3[1][i] != arr2[i]:
                verifyFlag = False

        if verifyFlag == True:
            print("Test #3: CORRECT")
        else:
            print("Test #3: INCORRECT")
    else:
        print("Test #3: INCORRECT")

# Time how long it takes to partition into two parts given an array
def timePartition():
    print("Time Partition")
    

if __name__ == "__main__":
    testingPartition()

    # timePartition()