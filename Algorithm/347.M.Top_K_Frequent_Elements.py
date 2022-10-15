class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = dict(Counter(nums))
        hm = sorted(hm.items(), key = lambda item : item[1], reverse=True)
        output = []
        for i in range(k) : 
            output.append(hm[i][0])
        return output