class Solution:
    def isPalindrome(self, x: int) -> bool:
        n,y = x,0
        f = lambda : (y * 10) + n % 10
        while n > 0:
            n , y = n//10, f()
        return y == x
            