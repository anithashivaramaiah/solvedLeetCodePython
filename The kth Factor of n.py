
#The kth Factor of n

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fact = []
        for i in range(1, n+1):
            if n % i == 0:
                fact.append(i)
        length = len(fact)
        if k > length:
            return -1
        else:
            return fact[(k-1)]
        
