def factorial(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i

    return pr


n = int(input())
print(factorial(n))
