def check_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        return True
    return False


for i in range(600851475143, 0, -2):
    if 600851475143 % i == 0:
        if check_prime(i):
            print(i)
            break
