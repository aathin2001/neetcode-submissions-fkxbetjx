class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        buck=[0] * 26

        for i in magazine:
            buck[ord(i)-ord('a')] +=1

        for i in ransomNote:
            buck[ord(i)-ord('a')] -=1


            if buck[ord(i)- ord('a')] <0 :
                return False

        return True