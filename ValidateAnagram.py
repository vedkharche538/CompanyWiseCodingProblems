from collections import Counter
s = "anagram" 
a = "nagarma"


def valid_anagram(s,a):
    return False if len(s) != len(a) else Counter(s) == Counter(a)


result = valid_anagram(s, a)
print(result)