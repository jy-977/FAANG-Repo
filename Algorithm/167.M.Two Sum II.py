class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #prob analysis
        #1) big range : bitmask ,hash, binaray search (sorted), two pointers, sliding window
        #2)one solution : 답 알자마자 return
        
        hashmap ={}
        for idx in range(len(numbers)) : 
            pair = target - numbers[idx]
            if(pair in hashmap) :
                return [ hashmap[pair],idx+1]
            else : 
                hashmap[numbers[idx]] = idx+1
