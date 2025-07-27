str = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Primary Solution
def group_anagram(str):
    new_anagram = dict()
    for idx in range(len(str)):
        new_anagram[str[idx]] = ''.join(sorted(str[idx]))
    grouped = dict()
    for key, val in new_anagram.items():
        if val in grouped:
            grouped[val].append(key)
        else:
            grouped[val] = [key]
    result = []
    return [val for val in grouped.values()]

# result = group_anagram(str)
# print(result)
# Time Complexity = O(n *k log n) where k is a length of each string in a list
# Space Complexity = O(n * k)

from collections import defaultdict

def group_anagram_optimized(strs):
    grouped = defaultdict(list)
    for s in strs:
        # Build a tuple of counts for 26 lowercase letters
        count = [0] * 26
        for c in s:
            count[ord(c)-ord('a')] += 1
        print(count)
        grouped[tuple(count)].append(s)
    return list(grouped.values())

print(group_anagram_optimized(str))

# Time Complexity = O(n *k) where k is a length of each string in a list
# Space Complexity = O(n * k)