primes=[2]

for i in range(3,2000001):
    print(i)
    for p in primes:
        if i%p==0:
            break
    else:
        primes.append(i)
        print(primes)

sumprimes=sum(primes)
print(sumprimes)