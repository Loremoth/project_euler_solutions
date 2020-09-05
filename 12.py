i = 0
num = 0
min_number_with_fifty_divisors = 1
for i in range(1, 51):
    min_number_with_fifty_divisors *= i

while True:
    def check_divisors(n):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1


        if count > 500:
            return True
        return False


    i = i + 1
    num += i

    if check_divisors(num):
        break

