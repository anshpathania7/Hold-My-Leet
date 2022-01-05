class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        nums.sort()
        for i in range(len(nums)):
            # Never let i refer to the same value twice to avoid duplicates.
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    j+=1
                    # Never let j refer to the same value twice (in an output) to avoid duplicates
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                else:
                    k-=1
        return output