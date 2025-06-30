def task(arr):
    res = 0
    n = len(arr)
    for i in range(n):
        res += 10 ** (n - i - 1) * arr[i]
    print(res)

task([8, 3, 5, 1])