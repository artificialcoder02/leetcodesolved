class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        t = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                t[j][i]=matrix[i][j]
        return t
