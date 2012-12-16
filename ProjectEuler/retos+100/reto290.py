'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time

def sumaDigitos(n):
    suma = 0
    while(n>9):
        suma += n%10
        n /= 10
    suma +=n
    return suma

def digitos(n):
    res = []
    while(n>9):
        res.append(n%10)
        n /= 10
    res.append(n)
    return res

def reto290():
    res = 0
    i = 1
    while i != 10**18:
#        lista = digitos(i)
#        suma1 = sum(lista)
#        suma2 = sum([11*d for d in lista])
        suma1 = sumaDigitos(i)
        suma2 = sumaDigitos(137*i)
        if suma1 == suma2:
            res += 1
        if i%1000000 == 0: print i
        i += 1
    print res
    
if __name__ == '__main__':
    ini = time()
    reto290()
    print "Tiempo =",time()-ini,"sg"