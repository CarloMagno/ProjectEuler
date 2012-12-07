'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time
import math

def factorization(k):
#    s = 2
#    fs = []
#    fs = set(fs)
#    powers = []
#    for j in range(s, int(math.sqrt(k))+1):
#        while k%j == 0:
#            #fs.append(j)
#            fs.add(j)
#            k = k // j
#    if (k != 1):
#        fs.add(k)
#    return list(fs)
    s = 2
    fs = []
    for j in range(s, int(math.sqrt(k))+1):
        while k%j == 0:
            fs.append(j)
            k = k // j
    if (k != 1):
        fs.append(k)
    powers = [fs.count(i) for i in set(fs)]
    return list(set(fs)),powers

def divisoresPropios(n):
    lista=[]
    for i in range(1,(n/2)+1):
        if (n%i)==0:
            lista.append(i)
    lista.append(n)
    return lista

def sigma2(n):
    #return sum([i**2 for i in divisoresPropios(n)])

    res = 1
    pi,ni = factorization(n)
    for i in range(len(pi)):
        res *= (pi[i]**(ni[i]+1)-1)/(pi[i]-1)

    return res
    
def SIGMA2(n):
    res = 1
    for i in range(2,n+1):
        print sigma2(i)
        res += sigma2(i)
        
    return res    

def reto401():
    return SIGMA2(10**15)%10**9

if __name__ == '__main__':
    ini = time()
    #reto401()
    
    print "sigma2(6) =",sigma2(6)
    print "SIGMA2(6) =",SIGMA2(6)
    print "Tiempo =",time()-ini,"sg"