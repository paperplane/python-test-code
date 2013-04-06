solution 1:

    from math import sqrt
    N = 100
    [p for p in range(2,N) if 0 not in [p%d for d in range(2,int(sqrt(p)+1))]]

solution 2:

    import math  
 
    def isPrime(n):  
        if n <= 1:  
            return False 
        for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:  
            return False 
        return True 
