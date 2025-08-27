import math
arr = [-2, 6, -3, -10, 0, 2]

max_prod = arr[0]
curr_max = arr[0]
curr_min = arr[0]
for num in arr[1:]:
    temp_max = max(num, curr_max*num, curr_min*num)
    curr_min = min(num, curr_max*num, curr_min*num)
    curr_max = temp_max
    max_prod = max(curr_max, max_prod)
print(max_prod)

