"""
CSCI 6212 - Project 3
The George Washington University

---
Pseudo-polynomial Partition
---
Given a set consisting of n integers, partition it into two parts so 
that the sum of the two parts is equal. The time complexity of this
algorithm should be O(ns) or better. Where s is the sum of the integers
in the set.
"""


def partition(arr):
    total_sum = sum(arr)
    target_sum = total_sum // 2
    left = 0
    right = len(arr) - 1
    left_sum = arr[left]
    right_sum = arr[right]

    while left < right:
        if left_sum == target_sum:
            return (arr[:left+1], arr[left+1:])
        elif left_sum < target_sum:
            left += 1
            left_sum += arr[left]
        else:
            right -= 1
            right_sum += arr[right]

        if right_sum == target_sum:
            return (arr[:right], arr[right:])
        elif right_sum < target_sum:
            right -= 1
            right_sum += arr[right]
        else:
            left += 1
            left_sum += arr[left]

    return None
