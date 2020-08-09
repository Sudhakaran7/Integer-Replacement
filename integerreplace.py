class Solution(object):
    def integerReplacement(self, n):
        if n == 1: return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n / 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

val=Solution()
n=int(input())
print(val.integerReplacement(n))
