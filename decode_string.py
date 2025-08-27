"""
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

"""


def decode_string(s):
    stack = []
    i = 0
    temp_s = ""
    s = s.replace("[", "").replace("]", "")
    while True:
        # print(f"pricessing for i the element{s[i]}")
        if i > len(s) - 1:
            counter = stack.pop()
            stack.append(temp_s * counter)
            temp_s = ""
            break
        if temp_s and s[i].isdigit() and stack:
            counter = stack.pop()
            stack.append(temp_s * counter)
            temp_s = ""
        if s[i].isdigit():
            stack.append(int(s[i]))
        elif s[i].isalpha():
            temp_s += s[i]
        i += 1
    # if temp_s and stack:
    #     c = stack.pop()
    #     stack.append(temp_s*c)
    #     temp_s = ""
    return "".join(stack)


result = decode_string("2[abc]3[cd]ef")
# print(result)

