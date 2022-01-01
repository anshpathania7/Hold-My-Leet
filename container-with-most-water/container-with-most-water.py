class Solution:
    
    def getWaterStored(self,l1,l2,b):
        if l1>l2:
            return l2*b
        else:
            return l1*b
    
    def maxArea(self, height: List[int]) -> int:
        l=0
        r= len(height)-1
        maxx=0
        while l!=r:
            height_at_l = height[l]
            height_at_r = height[r]
            water_stored = self.getWaterStored(height_at_r, height_at_l, r-l)
            if water_stored>maxx:
                maxx=water_stored
            if height_at_l < height_at_r:
                l+=1
            else:
                r-=1
        return maxx