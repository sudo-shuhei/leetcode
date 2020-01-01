class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return self.recursion(N,K)

    def recursion(self,n,k):
        if n == 1:
            return 0
        if k > 2**(n-2):
            return 1-self.recursion(n-1, k - 2**(n-2))
        else:
            return self.recursion(n-1, k)
