from typing import List

"""
Two sum
leetcode url: https://leetcode.com/problems/two-sum/
"""


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                # print('checking pair: ', i, j, nums[i], nums[j])
                pair_sum = nums[i] + nums[j]
                if pair_sum == target:
                    res = [i, j]
                    break
        return res


def main():
    # array = [2, 7, 11, 15]
    # target = 9

    array = [2, 7, 11, 15, 22, 3, 87, 98, 66, 36, 18]
    target = 77

    s = Solution()
    print(s.two_sum(array, target))


if __name__ == "__main__":
    main()
