from numpy import genfromtxt

my_data = genfromtxt('data/13.csv', delimiter='')
print(my_data)
sum=0
for i in my_data:
    sum+=i

print(sum)