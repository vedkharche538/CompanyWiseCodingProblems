# arr = [10, 7, 5, 8, 11, 9]
# maxprofit = 0
# minnum = float("inf")
# i = 0
# while i < len(arr):
#     minnum = min(arr[i], minnum)
#     maxprofit = max(arr[i] - minnum, maxprofit)
#     i+=1
# Find a subarray which will be having a max sum
# [2], [2,3], [2,3,5], [2,3,5,-2], [2,3,5,-2,7], [....-4]
# nums = [2, 3, 5, -2, 7, -4]

# sumn = 0
# max_sum = 0
# for i in range(len(nums)):
#     sumn += nums[i]
#     if sumn > max_sum:
#         max_sum = sumn
#     if sumn <0:
#         max_sum = 0

# from collections import Counter

# nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
# print(Counter(nums))

# Find the N th root of M where N=3 and M=27
# N = 3
# M = 27
# n = N
# counter = 0
# while True:
#     counter +=1
#     if M == n:
#         print(counter)
#         break
#     elif M < n:
#         print(-1)
#         break
#     n = n*N


# low = 1
# high = M

# while low <= high:
#     mid = (low+high)//2
#     if N**mid == M:
#         print("FOund!!")
#         break

#     if N**mid > M:
#         high = mid
#     else:
#         low = mid+1

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.
"""
# nums = [1, 3, 5, 6]
# target = 0
# left = 0
# right = len(nums) - 1
# mid = 0
# while left <= right:
#     mid = (left + right) // 2
#     if nums[mid] == target:
#         print(mid)
#         break
#     if nums[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# else:
#     if left >= len(nums):
#         print(mid+1)
#     elif left < target:
#         print(mid+1)
#     else:
#         print(mid)


"""
Search a 2D metrix
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3


# row, col = len(matrix), len(matrix[0])
# low, high = 0, row * col - 1

# while low <= high:
#     mid = (low + high) // 2
#     targetRow = mid // col
#     targetCol = mid % col
#     print(targetRow, targetCol)
#     if matrix[targetRow][targetCol] == target:
#         print(True)
#         break
#     elif matrix[targetRow][targetCol] > target:
#         high = mid - 1
#     else:
#         low = mid + 1


"""
Suppose an array of length n sorted in 
ascending order is rotated between 1 and n times.
 For example, the array nums = [0,1,2,4,5,6,7] might become:

"""
# nums = [3,4,5,1,2]
# left = 0
# right = len(nums) -1
# while left < right:
#     mid = (left+right)//2
#     if nums[mid] > nums[right]:
#         left = mid+1
#     else:
#         right = mid
# print(nums[left], left)

"""
search the element in rotated array
"""
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 10


def search_rotate_array(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return -1


#print(search_rotate_array(nums, target))


##
# arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# max_w = 0
# num_zeros = 0
# k = 2
# n = len(arr)
# l = 0
# for r in range(len(arr)):
#     if arr[r] == 0:
#         num_zeros += 1

#     while num_zeros > k:
#         if arr[l] == 0:
#             num_zeros -= 1
#         l += 1
#     w = r - l + 1
#     max_w = max(max_w, w)
# print(max_w)



###################################

def count_find_4_in_digit(nums):
    cnt = 0
    for i in range(nums):
        if '4' in str(i):
            cnt +=1
    return cnt

# print(count_find_4_in_digit(3))

from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    # def area(self):
    #     return 0.5 * self.base * self.height

# Example usage:
rect = Rectangle(10, 20)
tri = Triangle(10, 10)
print("Rectangle Area:", rect.area())
# print("Triangle Area:", tri.area())