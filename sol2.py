def isValid(s):
    stack = []
    asterisks = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == '*':
            asterisks.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            elif asterisks:
                asterisks.pop()
            else:
                return False

    while stack and asterisks:
        if stack[-1] > asterisks[-1]:
            return False
        stack.pop()
        asterisks.pop()

    return len(stack) == 0

# Example usage
s = "()"
result = isValid(s)
print(result)
