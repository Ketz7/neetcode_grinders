# import re

# Two ways to think here, the first part is how we can get the alphanumerical value out of the string.
# So either use regex or use ascii characters, there's also the isalpha() function in python that returns true or false which is inbuilt
# But feels like cheating, so I stay away from it, at least for the interview question.
# The second part is to use two pointers one at the start and one at the end, compare them till they meet each other and you'll have your answer.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pattern = re.compile('[\W_]+')
        # x = pattern.sub('', s.lower())
        # y = len(x) - 1 
        # for z in range(len(x)):
        #     start = x[z]
        #     end = x[y]
        #     y -= 1
        #     if start != end:
        #         return False
        # return True
        l,r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isalphanum(s[l]):
                l += 1
            while r > l and not self.isalphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l + 1, r - 1
        return True

    def isalphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
