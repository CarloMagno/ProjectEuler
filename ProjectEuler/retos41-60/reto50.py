'''
Created on 29/11/2012

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms,
and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?

@author: Carlitos
'''
from time import time

def criba_eratostenes(n):
    multiplos = set()
    res = []
    for i in range(2, n+1):
        if i not in multiplos:
            res.append(i)
            multiplos.update(range(i*i, n+1, i))
    return res

def encuentraSuma(primos):
    longitud = 0
    res = 0
    ultimo = primos[-1]
    numPrimos = len(primos)//100
    for i in reversed(range(numPrimos)):
        k = 0
        for j in range(0,numPrimos-i+k):
            suma = sum(primos[j:i+j:])
            k += 1
            if suma < ultimo:
                if suma in primos:
                    if i > longitud:
                        res = suma
                        longitud = i
                        return res, longitud
        if i%100 == 0: print i
if __name__ == '__main__':
    ini = time()
    N = 1000000
    longitud = 0
    res = 0
    primos = criba_eratostenes(N)
    print ">> Primos generados","longitud:",len(primos)
    print ">> Comienza busqueda"
#    for i in range(len(primos)//2):
#        for j in range(i+1,len(primos)):
#            suma = sum(primos[i:j:])
#            if suma in primos:
#                if (j-i) > longitud:
#                    res = suma
#                    longitud = j-i
#                    print res, longitud


#    for i in reversed(range(len(primos))):
#        k = 0
#        for j in range(0,len(primos)-i+k):
#            suma = sum(primos[j:i+j:])
#            k += 1
#            if suma in primos:
#                if (i-j)+1 > longitud:
#                    res = suma
#                    longitud = i-j+1
#                    print res, longitud
    res,longitud = encuentraSuma(primos)
    print "Resultado =",res,"( longitud =",longitud,") en",time()-ini,"sg"
