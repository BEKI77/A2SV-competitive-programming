class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1.0:
            return True
        if n<1:
            return False
        else:
            return self.isPowerOfFour(n/4)