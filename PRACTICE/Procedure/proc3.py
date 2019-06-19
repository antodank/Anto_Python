def fibonacci(n):
    """Return the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b) # see below
        c = a + b
        a = b
        b = c
        #a, b = b, a+b
    
    return result

print(fibonacci(10))

