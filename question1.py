#sum of the diagonal elments and find the differece of the sum of both diagonal


import numpy as np


matrix=[
    [1,2,3],
    [4,5,6],
    [8,8,9]
]

print('matrix')
for row in matrix:
    print(row)
print()

sum_r=0
sum=np.trace(matrix)
# print(sum)

for i in range(len(matrix)):
    for j in range(len(matrix[i])-1,-1,-1):
        if len(matrix[i]) -1 -j==i:
            sum_r+=matrix[i][j]

dig_diff=abs(sum-sum_r)
print(dig_diff)




