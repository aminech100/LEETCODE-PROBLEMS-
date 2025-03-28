class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = ""
        minLen = len(strs[0])
        for i in strs:
            if len(i) < minLen:
                minLen = len(i)
        answer = False
        br = False
        for i in range(minLen):
            for j in range(len(strs)):
                if strs[0][i] == strs[j][i]:
                    answer = True
                else:
                    answer = False
                    br = True
                    break
            if br:
                break
            if answer:
                word += strs[0][i]
        return word