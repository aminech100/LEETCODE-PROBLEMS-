class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        count = 0
        while s[i] == ' ':
            i -= 1
        while s[i] != ' ':
            i -= 1
            count += 1
            if i < 0:
                break
        return count