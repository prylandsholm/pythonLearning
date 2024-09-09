sieve = [True] * 500
for i in range(2, 500):
    if sieve[i]:
        print(i)
        for j in range(i*i, 500, i):
            sieve[j] = False

