'''
Created on 08/11/2012

@author: Carlitos
'''
from time import time
import math

def isprime(n):
    '''
    Check if integer n is a prime
    @return: bool
    '''
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n%x == 0:
            return False
    return True

def nextPrime(n):
    res = n+1
    aux = False
    while not aux:
        if isprime(res):
            aux = True
        else:
            res += 1
    return res

def calculaFuncion3(p):
    aux = math.factorial(p-5)
    sum = 0
    for i in range(4,0,-1):
        sum += aux%p
        aux *= (p-i)
    sum += aux%p
    return sum%p 

# Iterative Algorithm (xgcd)
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def modinv(a, m):
    g, x, y = egcd(a, m) 
    return x % m

def calculaFuncion(p):
    aux = math.factorial(p-5)
    sum = 0
    for i in range(4,0,-1):
        sum += aux
        aux *= (p-i)
    sum += aux
    return sum%p 

def mcd(n, m):
    m_aux = n % m
    if(m_aux == 0):
        return m
    elif(m_aux == 1):
        return 1
    else:
        return mcd(m, m_aux)

#def calculaFuncion7(p):
#    return ((p-3)*reciprocalMod(8%p,p)%p)

def reciprocalMod(x, m):
    if m<0 or x<0 or x>=m:
        return None
    y = x
    x = m
    a = 0
    b = 1
    while y != 0:
        z = x % y
        c = a-x/y*b
        x = y
        y = z
        a = b
        b = c
    if x == 1:
        return (a)%m
    else:
        return None

def calculaFuncion8(p):
    menostres = modinv(p-2,p)%p
    menoscuatro = (menostres*modinv(p-3,p))%p
    menoscinco = (menoscuatro*modinv(p-4,p))%p
    
    return (menostres+menoscuatro+menoscinco)%p

def calculaFuncion9(p):
    return (modinv(p-24,p) + modinv(p+6,p) + modinv(p-2,p))%p

def S(p):
    k = 3*p % 8
    return (k*p - 3) // 8

if __name__ == '__main__':

    print "Comienza..."
    ini = time()    
#    i = 100
    i = 4
    fin = False
    aux = None
    sum = 0
    while not fin:
        aux = nextPrime(i)
        if aux >= 10000000:
            fin = True
        else:
            sum += calculaFuncion9(aux)
            i = aux
#    sum += 480
    print "Suma:",sum,"en",time()-ini,"sg"
