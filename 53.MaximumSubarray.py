class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = -float('inf')
        dp = 0
        for i in nums:
            dp += i
            max_sub = max(dp, max_sub)
            dp = max(dp, 0)
        print(max_sub)
        return max_sub
