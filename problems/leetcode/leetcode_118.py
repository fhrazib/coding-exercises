"""
Name: Pascal's Triangle
URL: https://leetcode.com/problems/pascals-triangle/
Tags: #array, #dictionary, #map, #DP
"""
from typing import List

_map = {1: [1], 2: [1, 1]}


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        for i in range(3, 31):
            previous_row = _map.get(i - 1)
            new_row = [1]
            for j in range(1, len(previous_row)):
                new_row.append(previous_row[j - 1] + previous_row[j])

            new_row.append(1)
            _map[i] = new_row

        result = []
        for i in range(1, num_rows + 1):
            row = _map.get(i)
            result.append(row)

        return result

#
# s = Solution()
# print(s.generate(4))

