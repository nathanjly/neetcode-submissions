class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if num in comps:
                return [comps[num], i]
            else:
                comps[compliment] = i
        return None