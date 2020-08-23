# nが素数かどうかを判定


def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = int(n**0.5)+1
    for p in range(3, m, 2):
        if n % p == 0:
            return False
    return True


n = 2
print(isPrime(n))