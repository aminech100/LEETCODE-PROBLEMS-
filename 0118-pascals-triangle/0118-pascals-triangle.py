from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        answer.append([1])
        for i in range(1,numRows):
            answer.append([1])
            while len(answer[i]) < i:
                j = len(answer[i])
                val = answer[i-1][j-1] + answer[i-1][j]
                answer[i].append(val)
            answer[i].append(1)
        return answer