class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_num_to_index = {}
        for i in range(len(nums)):
            if target - nums[i] in map_num_to_index:
                print(map_num_to_index)
                return [i,map_num_to_index[target-nums[i]]]
            else:
                map_num_to_index[nums[i]]=i