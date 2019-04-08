# 600851475143
from math import sqrt

nl = 600851475143
o = sqrt(600851475143)
pf = []
def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return True
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
    return True

for i in range(int(o)):
    if is_prime(i) and nl % i == 0:
        pf.append(i)
        print(pf)

print(pf[-1])
