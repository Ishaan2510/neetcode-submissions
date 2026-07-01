class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """takes O(n) space """
        # d = collections.defaultdict(int)
        # for i, val in enumerate(numbers):
        #     d[val] = i+1
        # for i, num in enumerate(numbers):
        #     rem = target - num
        #     if rem in d.keys():
        #         ans.append(i+1)
        #         ans.append(d[rem])
        #         break
        """O(1) space"""
        l , r = 0, len(numbers)-1
        while l < r:
            curr = numbers[l] + numbers[r]
            if curr == target:
                return [l+1,r+1]
            elif curr < target:
                l += 1
            else:
                r -= 1