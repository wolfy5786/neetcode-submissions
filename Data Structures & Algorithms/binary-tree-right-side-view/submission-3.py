# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        f1 = deque([root])
        f2 = deque()

        if root == None:
            return []

        while f1:
            while f1:
                node = f1.popleft()
                if len(f1)==0:
                    result.append(node.val)
                if node.left:
                    f2.append(node.left)
                if node.right:
                    f2.append(node.right)
            f1 = f2
            f2 = deque()

        return result
    

        