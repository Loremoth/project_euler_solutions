from numpy import genfromtxt

my_data = genfromtxt('data/11.csv', delimiter=' ')
print(my_data)
max_horiz = 0
max_vert = 0
max_upper_diag = 0
max_lower_diag = 0

for i in range(my_data.shape[0]):
    for j in range(my_data.shape[1]):
        try:
            max_horiz = max( \
                my_data[i][j] * my_data[i + 1][j] * my_data[i + 2][j] * my_data[i + 3][j], max_horiz)
            max_vert = \
                max(my_data[i][j] * my_data[i][j + 1] * my_data[i][j + 2] * my_data[i][j + 3], max_vert)
            max_upper_diag = max(
                my_data[i][j] * my_data[i - 1][j + 1] * my_data[i - 2][j + 2] * my_data[i - 3][j + 3],
                max_upper_diag
            )
            max_lower_diag = max(
                my_data[i][j] * my_data[i + 1][j + 1] * my_data[i + 2][j + 2] * my_data[i + 3][j + 3],
                max_lower_diag
            )
        except IndexError as ie:
            continue

print(max_horiz)
print(max_vert)
print(max(max_horiz,max_vert,max_upper_diag,max_lower_diag))
