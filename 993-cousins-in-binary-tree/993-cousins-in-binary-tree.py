# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    #Array will hold [current root , current level]
    #for corresponding numbers x and y
    def __init__(self):
        self.x=[None,None]
        self.y=[None,None]
    
    
    def markPositions(self,root,x,y,currentLevel):
        if root==None:
            return
        left_val = root.left.val if root.left!=None else 0
        right_val = root.right.val if root.right!=None else 0
        if left_val==x or right_val==x:
            self.x=[root,currentLevel+1]
        if right_val==y or left_val==y:
            self.y=[root,currentLevel+1]
        self.markPositions(root.left,x,y,currentLevel+1)
        self.markPositions(root.right,x,y,currentLevel+1)
    
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.markPositions(root,x,y,0)
        #checking if root for both x,y are not same and current level of both x,y are same
        return self.x[0]!=self.y[0] and self.x[1]==self.y[1]
        