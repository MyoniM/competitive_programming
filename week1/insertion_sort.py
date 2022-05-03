import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for i in range(n):
        temp = arr[i]
        j = i 
        while (j>0 and arr[j-1]>temp): 
            arr[j]= arr[j-1] 
            j = j-1
            print(*arr)
        arr[j] = temp
    print(*arr)
    return

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
