arr = [[1,2,3], [4,5,6],[7,8,9]]


for i in range(len(arr)):
    for j in range(i+1, len(arr[0])):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # print(arr)
n = len(arr)
for i in range(len(arr)):
    for j in range(n//2):
        arr[i][j], arr[i][n-j-1] = arr[i][n-j-1], arr[i][j]
print(arr)