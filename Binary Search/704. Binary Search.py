class Solution:
    def search(self, nums: List[int], target: int) -> int:
        d={}
        for i,n in enumerate(nums):
            d[n]=i
        for value,keys in d.items():
            if target == value:
                return keys
                break
        else:
            return -1