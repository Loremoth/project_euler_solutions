for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if a * a + b * b == c * c and a < b < c and a+b+c==1000:
                print(a * b * c)
