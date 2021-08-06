from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        r = list(map(int, str(int(''.join(map(str, digits))) + 1)))

        print(r)


s = Solution()
a = [1, 2, 3]
b = [4, 3, 2, 1]
c = [1, 2, 8, 9]
e = [1, 2, 8, 9, 9]
f = [9, 9, 9]
g = [0]
s.plusOne(e)
