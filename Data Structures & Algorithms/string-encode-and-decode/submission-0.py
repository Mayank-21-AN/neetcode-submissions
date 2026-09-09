class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        
        for i in strs:
            encode_str += (f"{len(i)}#{i}")
        return encode_str


    def decode(self, s: str) -> List[str]:
        
        i = 0
        result = []
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            i = j + 1 + length
            result.append(word)
        return result
