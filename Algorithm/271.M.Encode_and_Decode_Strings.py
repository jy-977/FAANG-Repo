#50ms 99.93 faster
#14.1Mb 98.71 less

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return '\n'.join(strs)

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        return s.split('\n')
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# ---requirement----- 
# system design
# encode 실행 후 decode 실행
# input => encode => decode => output 

# 256 charaters valid ASCII 힌트 이해를 못하겠음
#여기에 속하지 않는 문자가 있음?


#IDEA : NON_ASCII---------
#decode split 어떻게 구분할지?
#NON ASCII 코드로 구분함
#근데 뭐가 NON_ASCII 인지 몰랐다 : 명령어 \n \t 이런거
