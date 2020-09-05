primes = [2, 3, 5, 7, 11, 13]
num=15
while True:
    for p in primes:
        if num%p==0:
            break
    else:
        primes.append(num)
        if len(primes)==10001:
            print(primes[10000])
            break
    num+=2
    print(num)
    print(len(primes))
