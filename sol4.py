class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def str2tree(s):
    def helper(s, start, end):
        if start > end:
            return None

        # Find the value of the current node
        val_end = start
        while val_end <= end and s[val_end] not in ('(', ')'):
            val_end += 1
        val = int(s[start:val_end])

        node = TreeNode(val)

        # Find the indices of left and right child substrings
        left_start = val_end
        left_end = find_matching_parenthesis(s, left_start)
        node.left = helper(s, left_start + 1, left_end - 1)

        right_start = left_end + 2
        right_end = find_matching_parenthesis(s, right_start)
        node.right = helper(s, right_start + 1, right_end - 1)

        return node

    def find_matching_parenthesis(s, start):
        count = 1
        i = start + 1
        while i < len(s):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
                if count == 0:
                    return i
            i += 1

        return -1

    if not s:
        return None

    return helper(s, 0, len(s) - 1)


def preorderTraversal(root):
    if not root:
        return []

    result = [root.val]
    result.extend(preorderTraversal(root.left))
    result.extend(preorderTraversal(root.right))

    return result


# Driver code
s = "4(2(3)(1))(6(5))"
root = str2tree(s)
result = preorderTraversal(root)
print(result)
