class Solution:
    def rob(self, nums: List[int]) -> int:

        a,b=0,0
        for i in range(len(nums)):
            a,b = max(a,nums[i]+b),a
        return max(a,b)
        