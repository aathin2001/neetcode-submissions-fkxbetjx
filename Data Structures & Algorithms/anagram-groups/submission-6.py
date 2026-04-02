class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result={}           #store the sorted(anagram) : [strings] values

        for i in strs:      #iterate each string
            s = tuple(sorted(i))        #create an tuple (sorted(anagram)) 
            result[s] = result.get(s,[])+[i]        #result[s]('a'c't') : result.get(s(serach for key ),[]if not set an default value) + [i] (append the string)

        return list(result.values())        # return the values of the hashmap

        