'''
Created on 29/11/2012

If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

@author: Carlitos
'''
from time import time

N = 1000

def numSoluciones(perim):
    pass

if __name__ == '__main__':
   ini = time()
   res = 0
   for i in range(120,N+1):
       num = numSoluciones(i)
       if res < num: 
           res = num
   print "Resultado =",res,"en",time()-ini,"sg" 