def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
    return True

print(sum([i for i in range(1, 2000000) if is_prime(i)]))