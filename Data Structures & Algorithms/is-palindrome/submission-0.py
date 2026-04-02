class Solution:
    def isPalindrome(self, s: str) -> bool:
        
       s = (''.join(char for char in s if char.isalpha() or char.isalnum() )).lower()

       return s == s[::-1]

