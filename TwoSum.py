nums = [2,7, 11, 15]
target=22

# Need to find a exactly one solution
def two_sum(nums, target):
    d = dict()
    for idx, num in enumerate(nums):
        if target-num in d:
            return [d[target-num], idx]
        else:
            d[num] = idx
    return -1

# result = two_sum(nums, target)
# print(result)

# Time Complexity = O(n)
# Space Complexity = O(n)

# what if they wanted to know all the index which is making this sum
new_num = [6,7,4,5]
new_target = 11
# output = [[0,3],[1,2]]
def upgrade_two_sum(nums, target):
    d = dict()
    result = []
    for idx, num in enumerate(nums):
        if target-num in d:
            result.append([d[target-num], idx])
        else:
            d[num] = idx
    return result

response = upgrade_two_sum(new_num, new_target)
print(response)