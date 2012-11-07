'''
Created on 07/11/2012

@author: Carlitos
'''
from itertools import product
from time import time

def rotate(n):
    m = 1
    while (n / m > 10):
        m = m * 10
    return ((m * (n % 10)) + n / 10)

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def esPrimoCircular(elem, candidatos):
    res = True
    res = res and isprime(elem)
    aux = str(elem)
    for i in range(len(aux)):
        aux = rotate(int(aux))
        res = res and isprime(rotate(aux)) and (rotate(aux) in candidatos)
    return res

def generarCandidatos():
    res = [1, 2, 3, 5, 7]
    for i in range(2,7):
        res.extend([reduce(lambda x,y: int(x)*10+int(y), n) for n in product("1379",repeat=i)])
    return res

if __name__ == '__main__':
    inicio = time()
    candidatos = generarCandidatos()
    res = 0
    for elem in candidatos:
        if esPrimoCircular(elem, candidatos):
            res += 1
    print time()-inicio, "sg"
    print res