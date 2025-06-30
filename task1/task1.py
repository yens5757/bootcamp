# Task: Given a list of digits, determine the integer that it represents. 
# For example, given the list: [8,3,5,1], your program should output 8351 as an integer.

def task(arr):
    res, n = 0, len(arr)
    for i in range(n):
        res += 10 ** (n - i - 1) * arr[i]
    print(res)

task([8, 3, 5, 1])

# 8351
# Each digit has a place value