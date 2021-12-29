class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter=1
        prevIdx,currIdx=0,1
        while currIdx<len(nums):
            if nums[currIdx]!=nums[prevIdx]:
                prevIdx=currIdx
                counter+=1
                nums[counter-1]=nums[prevIdx]
            currIdx+=1
        return counter
                
                
        