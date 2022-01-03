class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()       
        """
        count=0
        
        #First, put all 0s to start
        for i in range(len(nums)):
            if nums[i]==0:
                nums[count],nums[i] = 0, nums[count]
                count+=1
        #Now Putting all 1st after 0s
        for i in range(len(nums)):
            if nums[i]==1:
                nums[count],nums[i] = 1, nums[count]
                count+=1
        """
        
