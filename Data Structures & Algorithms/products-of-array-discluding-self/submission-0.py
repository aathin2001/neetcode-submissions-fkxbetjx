class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res ={}
        n1=n2=1             #asighning n1 and n2 = 1
                                                                #_____ <- this part if i = 3  
        for i in range(len(nums)):  #prefix (left multiplication) [1,2 |,3,4,5]  this iterate left to right
            res[i] = res.get(i,1) * n1

            n1 *= nums[i]           #multiplying previous n1 value with nums 
                                                                                              #____ <- this part
        for j in  range(len(nums)-1,-1,-1): # this one iterate right to left gor sufix [1,2,3,|4,5]
            res[j] = res.get(j,1) * n2

            n2 *= nums[j]                                                                  

        return list(res.values())

