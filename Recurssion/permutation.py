# Generate all possible permutations of an array or string (e.g., [1, 2, 3] → [1, 2, 3], [1, 3, 2], [2, 1, 3], etc.).


def permutation(ip, op):
    if not ip:
        print(op, end=", ")
        return
    for i in range(len(ip)):
        new_ip = ip[:i] + ip[i + 1 :]
        new_op = op + [ip[i]]
        permutation(new_ip, new_op)


# permutation([1,2,3], [])


def permutation_backtrack(arr, start=0):
    if start == len(arr):
        print(arr, end=", ")
        return
    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]
        # print("before backtracking", arr)
        permutation_backtrack(arr, start + 1)
        arr[start], arr[i] = arr[i], arr[start]  # backtrack
        # print("after backtracking", arr)


permutation_backtrack([1, 2, 3])
# permutation_backtrack("abcd", 0)
