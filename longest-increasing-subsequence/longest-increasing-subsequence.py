from bisect import bisect_left

class Solution:
    #Uses binary search to get position of element which is just greater than n
    def getIndexOfNextGreaterElement(self, n, dp)->int:
        pos = bisect_left(dp,n)
        if pos==len(dp):
            return None
        else:
            return pos
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[]
        for i in range(len(nums)):
            index = self.getIndexOfNextGreaterElement(nums[i],dp)
            
            if index is None:
                dp.append(nums[i])
            else:
                dp[index] = nums[i]
        return len(dp)
