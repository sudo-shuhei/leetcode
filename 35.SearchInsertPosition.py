class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0
        if len(nums) ==1:
            if nums[0] >= target:
                return 0
            elif nums[0] < target:
                return 1


        while True:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif high - low == 1 and target <= nums[low]:
                return 0
            elif high - low == 1 and target > nums[high]:
                return len(nums)
            elif high - low == 1:
                return high
            elif nums[mid] > target:
                high = mid
            else:
                low = mid
