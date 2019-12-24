import numpy as np
import bisect

class Solution: #最長増加部分列
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [np.inf]*len(nums)
        for i in nums:
            index = bisect.bisect_left(dp, i)
            dp[index] = i
            # print(dp)
        result = 0
        for i in dp:
            if i != np.inf:
                result += 1
        return result
