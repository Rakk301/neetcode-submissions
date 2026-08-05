class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal =[[1]]
        for i in range(1,numRows):
            subpascal = [1]
            for j in range(i-1):
                subpascal.append(pascal[i-1][j]+pascal[i-1][j+1])
            subpascal.append(1)
            pascal.append(subpascal)
        return pascal
