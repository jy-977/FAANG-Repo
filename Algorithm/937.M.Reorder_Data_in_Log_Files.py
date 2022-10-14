class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

#       40ms 92.45% faster / 13.8mb less
        lm = []
        dm = []
        
        for i in range(len(logs)) : 
#             digit // letter checker
            if((logs[i].split()[1]).isnumeric()) : 
                dm.append(logs[i])
            else : 
                lm.append(logs[i])
        #
        lm.sort(key =lambda item : (item.split()[1:], item.split()[0]) )
        return lm +dm