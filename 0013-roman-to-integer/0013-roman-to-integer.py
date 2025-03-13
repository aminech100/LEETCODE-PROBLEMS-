class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = 0
        i = 0
        while i + 1 < len(s):     #don't forget to add the last letter 
            if s[i] == "I" and s[i+1] == "V":
                result += 4
                i += 2
            elif s[i] == "I" and s[i+1] == "X":
                result += 9
                i += 2
            elif s[i] == "X" and s[i+1] == "L":
                result += 40
                i += 2
            elif s[i] == "X" and s[i+1] == "C":
                result += 90
                i += 2
            elif s[i] == "C" and s[i+1] == "D":
                result += 400
                i += 2
            elif s[i] == "C" and s[i+1] == "M":
                result += 900
                i += 2
            else:
                result += dct[s[i]]
                i += 1
        if i == len(s)-1:
            result += dct[s[i]]
        return result 