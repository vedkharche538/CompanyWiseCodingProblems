from collections import Counter
nums = [2,3,1,2,1,3]
k=2


def top_k_element(nums, k):
    f =  Counter(nums)
    return list(map(lambda x: x[0] , f.most_common(k)))

result = top_k_element(nums, k)
print(result)

# Time Complexity = O(n + u log k)
# Space Complexity = O(n)