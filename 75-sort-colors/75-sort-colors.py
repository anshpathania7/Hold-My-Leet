class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        
        #First, put all 0s to start
        for i in range(len(nums)):
            if nums[i]==0:
                nums[count],nums[i] = 0, nums[count]
                count+=1
        for i in range(len(nums)):
            if nums[i]==1:
                nums[count],nums[i] = 1, nums[count]
                count+=1
        
