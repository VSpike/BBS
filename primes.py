"""
From http://www.4dsolutions.net/cgi-bin/py2html.cgi?script=/ocn/python/primes.py
"""

import random

def bigppr(bits=256):
    """
    Randomly generate a probable prime with a given
    number of hex digits
    """
     
    candidate = random.getrandbits(bits) | 1  # Ensure odd

    prob = 0
    while 1:
        prob=pptest(candidate)
        if prob>0:
            return candidate
        candidate += 2
        
def pptest(n):
    """
    Simple implementation of Miller-Rabin test for
    determining probable primehood.
    """
    
    if n<=1: 
        return 0

    # if any of the primes is a factor, we're done
    bases  = [random.randrange(2,50000) for x in xrange(90)]

    
    for b in bases:
        if n%b==0: 
            return 0
        
    tests,s  = 0L,0
    m        = n-1

    # turning (n-1) into (2**s) * m

    while not m&1:  # while m is even
        m >>= 1
        s += 1

    for b in bases:
        tests += 1
        isprob = algP(m,s,b,n)
        if not isprob: 
            break
            
    if isprob: 
        return (1-(1./(4**tests)))
    
    return 0

def algP(m,s,b,n):
    """
    based on Algorithm P in Donald Knuth's 'Art of
    Computer Programming' v.2 pg. 395 
    """
    y = pow(b,m,n)    
    
    for j in xrange(s):
        if (y==1 and j==0) or (y==n-1):
            return 1
        y = pow(y,2,n)       
       
        return 0


