class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal =[[1]]
        for i in range(1, numRows):
            pairs = len(pascal[i-1])-1
            temp = [1]
            for j in range(pairs):
                temp.append(pascal[i-1][j] + pascal[i-1][j+1])
            temp.append(1)
            pascal.append(temp)
        return pascal