# class Solution:
#     def xorOperation(self, n: int, start: int) -> int:
#         a=0
#         nums=[0]*n
#         for i in range(0,n):
#             nums[i]=start +2*i
#         for j in range(0,n):
#             a=a^nums[j]
#         return a
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a=0
        for i in range(n):
            a^=start+2*i
        return a
