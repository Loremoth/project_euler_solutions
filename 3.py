primes = [2]
max = 0


def check_prime(n: int) -> bool:
    for i in primes:
        if n % i == 0:
            break
    else:
        return True
    return False


for i in range(3, int(600851475143 / 2), 2):
    if check_prime(i):

        primes.append(i)
        if 600851475143 % i == 0:
            max = i

print(max)