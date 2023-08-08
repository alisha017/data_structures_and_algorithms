#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numberOfItems' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY startIndices
#  3. INTEGER_ARRAY endIndices
#

def numberOfItems(s, startIndices, endIndices):
    # Write your code here
    print(s, startIndices, endIndices)
    if len(startIndices) != len(endIndices):
        return [0]
    count = []
    for i in range(len(startIndices)):
        substring = s[startIndices[i] - 1: endIndices[i]]
        print(substring)
        start = None
        move = 0

        current_count = None
        while move < len(substring):

            if substring[move] == '|':
                start = move
                if current_count is None:
                    current_count = 0

            if substring[move] == "*" and current_count is not None and start != move:
                current_count += 1

            move += 1
        count.append(current_count)
        print(count)
        return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    startIndices_count = int(input().strip())

    startIndices = []

    for _ in range(startIndices_count):
        startIndices_item = int(input().strip())
        startIndices.append(startIndices_item)

    endIndices_count = int(input().strip())

    endIndices = []

    for _ in range(endIndices_count):
        endIndices_item = int(input().strip())
        endIndices.append(endIndices_item)

    result = numberOfItems(s, startIndices, endIndices)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
