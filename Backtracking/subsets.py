class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output=[[]]
        for i in nums:
            output += [lst+[i] for lst in output]
        return output
    

        
        # [1]
        # [[],[1]]
        # 2**n - n -> no.of elements in the list

        # [1,2]
        # [[],[1],[2],[1,2]]

        # [1,2,3]
        # [[],[1],[2],[1,2],[3],[]]