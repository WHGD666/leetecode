class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_s=-inf
        s=0
        for i,x in enumerate(nums):
            s+=x
            left=i-k+1
            if left<0:
                continue
            max_s=max(max_s,s)
            s-=nums[left]
        return max_s/k
