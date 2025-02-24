# Time O(n)
# Space O(n)
from collections import deque
import math
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root == None: return result

        dq = deque()
        dq.append(root)
        while len(dq) > 0:
            size = len(dq)
            levelMax = -math.inf
            for i in range(size):
                node = dq.popleft()
                if levelMax < node.val: levelMax = node.val
                if node.left != None: dq.append(node.left)
                if node.right != None: dq.append(node.right)
            result.append(levelMax)
        return result
    

# Time O(n)
# Space O(h)
from collections import deque
class Solution:
    def __init__(self):
        self.result = []

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return self.result

        self.dfs(root, 0)
        return self.result
    
    def dfs(self, root: Optional[TreeNode], level: int) -> None:
        if root == None: return

        if len(self.result) < level+1: self.result.append(root.val)
        else: self.result[level] = max(self.result[level], root.val)

        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)