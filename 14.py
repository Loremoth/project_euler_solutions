max_length_collatz = 0
max_num=0

for num in range(2, 1000000):
    def length_collatz(n):
        count = 1

        while True:
            if n == 1:
                return count
            count += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1

    lcn=length_collatz(num)
    if lcn >= max_length_collatz:
        max_length_collatz = lcn
        max_num=num

print(max_num)
