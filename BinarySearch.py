nums = [-1, 0, 3, 5, 9, 12]
target = 5



def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) //2
        if arr[mid] ==  target:
            return mid
        
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1

result = binary_search(nums, target)
print(result)