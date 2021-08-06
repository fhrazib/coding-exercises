"""
Name: Valid Palindrome
URL: https://leetcode.com/problems/valid-palindrome/
Tags: #array
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_array = [c.lower() for c in s if c.isalnum()]

        start = 0
        end = len(char_array) - 1
        while start <= end:
            if char_array[start] != char_array[end]:
                return False
            start = start + 1
            end = end - 1

        return True

#
# s = Solution()
# s1 = "A man, a plan, a canal: Panama"  # True
# s2 = "race a car"  # False
# print(s.isPalindrome(s2))
