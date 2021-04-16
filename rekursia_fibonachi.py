def fib(n):
    if n <= 1:
        return n
    return (fib(n - 1) + fib(n - 2))

fib = [0, 1] + [0] * (n - 1)
for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib([i - 2])