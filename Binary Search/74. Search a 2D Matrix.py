class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        t=m*n
        l=0
        r=t-1

        while l<=r:
            M=(l+r)//2
            i=M//n
            j=M%n
            mid_num=matrix[i][j]

            if target == mid_num:
                return True
            elif target < mid_num:
                r=M-1
            else:
                l=M+1

        return False