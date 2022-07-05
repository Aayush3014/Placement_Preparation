class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rev = 0
        while num>0:
            d = num%10
            rev = rev*10+d
            num = num//10
        return rev == x