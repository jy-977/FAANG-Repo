class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
#        1262ms 40.66 / 28.5mb 13.47 less
        return  sum(damage)-min(armor,max(damage))+1