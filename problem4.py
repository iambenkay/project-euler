result = 1

def is_palindrome(n):
    n = str(n)

    if n == n[::-1]:
        return True
    return False

for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i*j) and (i * j) > result:
            result = i * j

print(result)