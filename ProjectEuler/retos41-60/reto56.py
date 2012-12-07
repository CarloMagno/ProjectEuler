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

def reto56():
    maximo = 0
    for a in range(2,100):
        for b in range(2,100):
            num = sumaDigitos(a**b)
            if num > maximo:
                maximo = num
                print maximo
    print "Resultado =",maximo

if __name__ == '__main__':
    ini = time()
    reto56()
    print "Tiempo =",time()-ini,"sg"