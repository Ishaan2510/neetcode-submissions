class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        d = collections.defaultdict(int)
        for i, val in enumerate(numbers):
            d[val] = i+1
        for i, num in enumerate(numbers):
            rem = target - num
            if rem in d.keys():
                ans.append(i+1)
                ans.append(d[rem])
                break
        return ans