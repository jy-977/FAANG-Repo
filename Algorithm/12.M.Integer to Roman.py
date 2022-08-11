class Solution:
    def intToRoman(self, num: int) -> str:
#       solution (58ms 84.05% faster, 13.9mb 80.25 less)
        symbol = ['M', 'CM','D','CD' ,'C','XC','L','XL' ,'X','IX', 'V', 'IV', 'I']
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        idx =0
        output =''
        for idx, val in enumerate(value):
            a = num//val
            
            for _ in range(a) : 
                output=output+symbol[idx]
            num = num%val
        return output
            