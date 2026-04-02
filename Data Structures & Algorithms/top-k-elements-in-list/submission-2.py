class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}             #store the freq  i.e the number occured (count)
        res = []

        for i in nums:
            freq[i] =freq.get(i,0) +1   #counter

        temp =[[freq[num],num] for num in freq]  # store the freq hashmap in list [count:num] for sort it later 

        for count,num in sorted(temp,reverse=1):   #append the k num of digits in res
            res.append(num)
            if len(res) >= k:                      # break the condition when the res[] reaches k  len(res)
                break

        return res 

