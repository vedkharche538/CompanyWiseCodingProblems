# Find all combinations of an array that sum to a target (e.g., [2, 3, 5] and target 8 → [3, 5]).
"""
I have a thinking where there are 3 options for each element
arr[i] we can include it once
arr[i] we can include it multiple time
or arr[i] we can exclude it and not include it in my comb
"""
target = 8
nums = [2,3,5]
def combination(arr, comb, i, target):
    if i == len(arr) or target <0:
        return
    if target ==0:
        print(comb)
        return
    
    comb.append(arr[i])
    combination(arr, comb, i+1, target-arr[i])
    combination(arr, comb, i, target-arr[i])
    comb.pop()
    combination(arr,comb, i+1, target)

combination(nums, [], 0, target)