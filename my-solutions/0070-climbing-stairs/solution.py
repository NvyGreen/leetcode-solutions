class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {0:1, 1:1}

        def f(n):
            if n in cache: return cache[n]
            if n <= 1:
                return 1
            else:
                cache[n] = f(n-1) + f(n-2)
                return cache[n]
            
        return f(n)
        

