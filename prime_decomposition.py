import time
i = 10
st1 = time.time()
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

print(prime_decomposition(i))

en1 = time.time()
print(en1-st1)

def prime_factorize(n):
    r = []
    while n % 2 == 0:
        r.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            r.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        r.append(n)
    return r
print(prime_factorize(i))

en2 = time.time()
print(en2-en1)