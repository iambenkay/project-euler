fib = [1, 2]

i = 0

while fib[-2] < 4000000:
    fib.append(fib[i] + fib[i+1])
    i += 1

print(sum([i for i in fib if i % 2 == 0]))