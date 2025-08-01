"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""

"""My Approach i think in mind at first it will be llike a using 2 pointers
since the list is sorted and we are expecting it to be as per the format we can do it with optimal time complexity
left, right pointers and my loop will run until left<=right 
"""

def naive_approach(arr):
    left =0
    right = len(arr)-1
    ans = []
    while left <= right:
        if arr[left] not in ans:
            ans.append(arr[left])
            left +=1
        if arr[right] not in ans:
            ans.append(arr[right])
            right -=1
        
    return ans
print(naive_approach([1,2,3,4,5]))
