# Task: Given a list of digits, determine the integer that it represents. 
# For example, given the list: [8,3,5,1], your program should output 8351 as an integer.


# Each digit has a place value, in the example of 8351. 8 is representing 1000*8, 3 is 100*3, 5 is 10*5, and 1 is 1*1
# By multiply each digit by its place value and add them together, we can get the integer that we want

def task(arr):
    res, n = 0, len(arr)
    for i in range(n):
        # this formula is using the current array item(arr[i]) multiply by the place value
        # 10 to the power of n-i-1, which is just how many item is there after this item.
        res += 10 ** (n - i - 1) * arr[i]
    print(res)

task([8, 3, 5, 1])