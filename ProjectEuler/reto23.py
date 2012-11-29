'''
Created on 27/11/2012

@author: Carlitos
'''
from time import time

def abundant(n):
    sum = 1
    for i in range(2,n//2+1):
        if n%i == 0:
            sum += i 
            if sum > n:
                return True
    return False
    
if __name__ == '__main__':
    ini = time()
    
    print "En",time()-ini,"sg"