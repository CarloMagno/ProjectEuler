'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time
from itertools import permutations
import math

def isPrime(n):
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
    
def reto41():
    res = 0
    n = 9
    found = False
    string = '987654321'
    while not found:
        lista = list(map("".join, permutations(string)))
        lista = filter(isPrime,[int(elem) for elem in lista])
        if lista == []:
            string = string[1:]
            print string
        else:
            res = max(lista)
            found = True
    print res
    
if __name__ == '__main__':
    ini = time()
    reto41()
    #print  max(filter(isPrime,[int(elem) for elem in list(map("".join, permutations('321')))]))
    print "Tiempo =",time()-ini,"sg"