from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return left


s = Solution()
a = [2, 3, 4, 5, 9, 23, 98, 103, 107]
b = [2, 3, 4]
print(s.searchInsert(a, 102))
