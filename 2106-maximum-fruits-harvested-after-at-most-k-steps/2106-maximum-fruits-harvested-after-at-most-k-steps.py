from collections import defaultdict
class Solution:
    
    def ans(self, A: List[List[int]], pos: int, k: int) -> int:
        r_b = max(pos, A[-1][0])    # right boundary.
        amt = [0] * (1 + r_b)
        for a, b in A:
            amt[a] = b
        
        presum = [0] + list(itertools.accumulate(amt))  # prefix sum 
        ans = 0
        
        for r_dist in range(min(k, r_b - pos) + 1):      # The right distance to start position.
            l_dist = max(0, k - 2 * r_dist)       # If we turn around, how far we can go left beyond start position.
            l_pos, r_pos = max(0, pos - l_dist), pos + r_dist    # The leftmost and rightmost position we can reach. 
            ans = max(ans, presum[r_pos + 1] - presum[l_pos])    # Get overall fruits within this range from presum.
        
        for l_dist in range(min(k, pos) + 1):
            r_dist = max(0, k - 2 * l_dist)            
            l_pos, r_pos = pos - l_dist, min(r_b, pos + r_dist)     
            ans = max(ans, presum[r_pos + 1] - presum[l_pos])
            
        return ans
    
    def getStartingPointsForRTHENL(self,startPos,k):
        if startPos-k<=0:
            left=0
            right= startPos + (k-startPos)//2
        else:
            left=startPos-k
            right=startPos
        return left,right
    
    
    def moveRightThenLeft(self,startPos,k,storeMap):
        l,r=self.getStartingPointsForRTHENL(startPos,k)
        firstEle=l
        secondEle=l+1
        allLeftSum=0
        maxSum=0
        for i in range(l,r+1):
            allLeftSum+=storeMap[i]
        while l < startPos:
            l+=2
            r+=1
            currSum = allLeftSum-storeMap[firstEle]-storeMap[secondEle]+storeMap[r]
            firstEle=l
            secondEle=l+1
            if currSum>maxSum:
                maxSum=currSum
        return maxSum
              
        
    def moveLeftThenRight(self,startPos,k,storeMap):
        l,r = startPos, startPos+k
        #each iter when l moves to left, we'll move r to left by 2 places
        #print(f"initial, l:{l} r:{r}")
        lastSum=0
        lastElementAdded=r
        secondLasrElementAdded=r-1
        #Sum when moved all towards Right
        for i in range(l,r+1):
            lastSum+=storeMap[i]
        #print(f"all right sum : {lastSum}\n\n")
        maxSum=lastSum
        
        
        #Sum when moving both left and right
        while r>startPos:
            l-=1
            r-=2
            currentSum = storeMap[l]+lastSum-storeMap[lastElementAdded]-storeMap[secondLasrElementAdded]
            #print(f"currentSum : {currentSum} for [{l} to {r}]\n")
            lastSum=currentSum
            lastElementAdded=r
            secondLasrElementAdded=r-1
            if currentSum>maxSum:
                maxSum=currentSum
        return maxSum
        
    def getMappedValue(self,fruits):
        storeMap = defaultdict(lambda:0)
        for val in fruits:
            storeMap[val[0]]=val[1]
        return storeMap
    
    
    
    
    def maxTotalFruits(self, fruits, startPos, k) -> int:
        
        return self.ans(fruits,startPos,k)
        
        storeMap = self.getMappedValue(fruits)
        moveLeftThenRightSum = self.moveLeftThenRight(startPos,k,storeMap)
        moveRightThenLeftSum = self.moveRightThenLeft(startPos,k,storeMap)
        
        return max(moveLeftThenRightSum,moveRightThenLeftSum)

