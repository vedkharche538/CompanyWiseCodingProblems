def characterReplacement(s: str, k: int) -> int:
    longest = 0
    l = 0
    counts = [0] * 26

    for r in range(len(s)):
        counts[ord(s[r]) - 65] += 1
        while (r - l + 1) - max(counts) > k:
            counts[ord(s[l]) - 65] -= 1
            l += 1

        longest = max(longest, (r - l + 1))

    return longest

longest_substring = characterReplacement("AABABBA", 2)
print(longest_substring)