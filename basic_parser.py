"""
"a[b[c]d[e]]" -> ['a', ['b', ['c'], 'd', ['e']]]

"""

def basic_parser(s):
    i = 0
    stack = []
    current = []
    token = ""

    for char in s:
        if char.isalnum():
            token += char
        elif char == '[':
            if token:
                current.append(token)
                token = ""
            stack.append(current)
            current = []
        elif char ==']':
            if token:
                current.append(token)
                token = ""
            prev = stack.pop()
            prev.append(current)
            current = prev
        else:
            if token:
                current.append(token)
                token = ""
    if token:
        current.append(token)
    return current


result = basic_parser("a[b[c]d[e]]")
print(*result)
