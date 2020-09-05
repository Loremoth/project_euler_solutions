firstsum = 0
secondsum = 0
for i in range(101):
    firstsum+=i*i
    secondsum+=i

secondsum*=secondsum

print(secondsum - firstsum)