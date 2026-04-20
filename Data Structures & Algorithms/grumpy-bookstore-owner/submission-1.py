class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        s=res=0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                s+=customers[i]

        print(s)
        
        for i in range(len(customers)-minutes+1):
            s1=s

            for j in range(i,minutes+i):
                # print(customers[[j]])
                if grumpy[j]:
                    s1+=customers[j]

            # print(customers[])

            res=max(res,s1)

        return res
                



            



        