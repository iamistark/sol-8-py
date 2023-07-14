def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        
        return len(set(s)) < len(s)


    diff_positions = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff_positions.append(i)

    
    return len(diff_positions) == 2 and s[diff_positions[0]] == goal[diff_positions[1]] and s[diff_positions[1]] == goal[diff_positions[0]]


s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)
