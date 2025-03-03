def solution(s):
    stack = []

    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    if len(stack) > 0:
        return False
    return True