'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time
import math

def criba_eratostenes(n):
    multiplos = set()
    res = []
    for i in range(2, n+1):
        if i not in multiplos:
            res.append(i)
            multiplos.update(range(i*i, n+1, i))
    return res

def isPrime(n):
    if n == 0:
        return False
    
    if n == 1:
        return True
    elif n < 4:
        return True
    elif n%2 == 0:
        return False
    elif n < 9:
        return True
    elif n%3 == 0:
        return False
    else:
        r = int(math.sqrt(n))+1
        f = 5
        while f <= r:
            if n%f == 0:
                return False
            if n%(f+2) == 0:
                return False
            f = f+6
        return True
    
def numTerminosPrimos(a,b):
    finish = False
    n = 0
    res = 0
    while not finish:
        val = n**2+a*n+b
        if isPrime(val):
            res += 1
            n += 1
        else:
            finish = True
        
    return res 
    
def reto27():
    maximo = 0
    maxA = 0
    maxB = 0
    conjuntoB = []
    conjuntoB = criba_eratostenes(1000)
#    for elem in criba_eratostenes(1000):
#        conjuntoB.append(-elem)
#        conjuntoB.append(elem)
#    conjuntoB = sorted(conjuntoB)
    
    for a in range(-1000,1000):
        for b in conjuntoB:
            num = numTerminosPrimos(a,b)
            if num >= maximo:
                maximo = num
                maxA = a
                maxB = b
                print "Maximo =",maximo
                print "a =",maxA
                print "b =",maxB
        if a%10 == 0: print a
    print "Resultado = ",maxA*maxB

if __name__ == '__main__':
    ini = time()
    reto27()
    print "Tiempo =",time()-ini,"sg"