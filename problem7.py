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

counter = 0
x = 1

while x > 0:
    if is_prime(x):
        counter += 1
    
    if counter == 10001:
        break
    x += 1

print(x)