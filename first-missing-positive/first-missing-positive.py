class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        totalElements = len(nums)
        map_nums = {}
        for i in range(totalElements):
            map_nums[nums[i]]=None
        min_pos_num = 1
        while totalElements>0:
            if min_pos_num in map_nums:
                min_pos_num+=1
            totalElements-=1
        return min_pos_num
        