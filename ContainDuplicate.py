from collections import Counter
nums = [1,2,3,1]

def contain_duplicates(nums):
    s =set()
    result = []
    for num in nums:
        if num not in s:
            s.add(num)
        else:
            result.append(num)
    return result

result = contain_duplicates(nums)
print(result)