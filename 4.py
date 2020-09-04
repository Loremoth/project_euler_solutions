last_pal = 0

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        k = i * j
        if k > last_pal:
            def check_pal(n: int) -> bool:
                for q in range(len(str(n))):
                    if str(n)[q] != str(n)[len(str(n)) - q-1]:
                        return False
                else:
                    return True

            if check_pal(k):
                last_pal = k

print(last_pal)