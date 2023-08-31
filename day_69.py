#Rotate Image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length=len(matrix) 
        for i in range(length):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j] 
        for row in range(length):
            matrix[row].reverse()