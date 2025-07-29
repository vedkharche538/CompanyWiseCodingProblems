# Use recursion to find the sum of all elements in an array.
def sum_of_elements(nums):
    if not nums:
        return 0
    
    return nums[0] + sum_of_elements(nums[1:])

print(sum_of_elements([1,2,3,4,5]))