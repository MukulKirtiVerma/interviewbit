class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        sx=""
        for i in A: sx=sx+str(i)
        return  list(str(int(sx)+1))