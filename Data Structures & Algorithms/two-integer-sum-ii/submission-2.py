class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        r_pntr= len(numbers) -1
        l_pntr= 0

        res = numbers[l_pntr] + numbers[r_pntr]

        while res != target:

            res = numbers[l_pntr] + numbers[r_pntr]

            if res > target :
                r_pntr -= 1

            elif res < target:
                l_pntr +=1
            
        if res == target :
            return [l_pntr + 1,r_pntr + 1] 

        
        