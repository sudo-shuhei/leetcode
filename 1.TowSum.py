from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #全探索 memory limit
        # comb = list(combinations(enumerate(nums), 2))
        # # print(comb)
        # for c in comb:
        #     if c[0][1]+c[1][1] == target:
        #         return [c[0][0],c[1][0]]

        #HashMap使用
        dict = {}
        for i,v in enumerate(nums):
            complement = target - v
            if complement in dict.keys():
                return [dict[complement], i]
            else:
                dict[v] = i
