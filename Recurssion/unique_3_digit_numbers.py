# Unique 3-Digit Even Numbers

def unique_3_digit_even_numbers(digits):
    ans = set()
    def backtrack(path, used):
        if len(path) == 3:
            if path[-1] % 2 == 0:
                num = path[0]*100 + path[1]*10 + path[2]
                ans.add(num)
            return
        for i in range(len(digits)):
            if used[i]:
                continue
            # Skip leading zero
            if len(path) == 0 and digits[i] == 0:
                continue
            used[i] = True
            backtrack(path + [digits[i]], used)
            used[i] = False
    backtrack([], [False]*len(digits))
    return sorted(ans)

# print(unique_3_digit_even_numbers([1,2,3,4]))
# arr = [1,2,3,4]
# def combination_of_numbers(path, start):
#     if len(path) == 3:
#         print(path)
#         return
#     for i in range(start, len(arr)):
#         combination_of_numbers(path + [arr[i]], i+1)
# combination_of_numbers([], 0)
arr = [1,2,3,4]
def permutation_of_numbers(path, used):
    if len(path) == 3:
        print(path)
        return
    for i in range(len(arr)):
        if not used[i]:
            used[i] = True
            permutation_of_numbers(path + [arr[i]], used)
            used[i] = False
    
permutation_of_numbers([], [False]*len(arr))