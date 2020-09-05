num = 20

while True:
    def divisible(n):
        for i in range(1, 21):
            if n%i!=0:
                return False
        else:
            return True

    num+=20
    if divisible(num):
        print(num)
        break