class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            sub = target - nums[i]
            if sub in hashmap.keys():
                return [hashmap[sub], i]
            hashmap[nums[i]] = i
        return []