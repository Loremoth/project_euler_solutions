fibo1 = 1
fibo2 = 2
fibo = 3
even =True
sum = 2

while fibo <= 4000000:
    even = not even
    if fibo % 2 == 0:
        sum += fibo
    fibo1 = fibo2
    fibo2 = fibo
    fibo = fibo1 + fibo2

print(sum)