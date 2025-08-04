"""
Given a string s, find the length of the longest substring without duplicate characters.

"""

s = "abcabcbb"


def longest_substring(s: str):
    track_unique = []
    left = 0
    right = 0
    max_size = 0
    while right < len(s):
        if s[right] not in track_unique:
            track_unique.append(s[right])  # type: ignore
        else:
            while s[right] in track_unique:
                track_unique.pop(0)
            track_unique.append(s[right])  # type: ignore
            left += 1
        right += 1
        max_size = max(max_size, len(track_unique))  # type: ignore
    return max_size


result = longest_substring(s)
