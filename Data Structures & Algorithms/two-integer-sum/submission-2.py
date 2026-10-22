class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            comp = target - num
            if num in hash:
                return [hash[num], i]
            hash[comp] = i
