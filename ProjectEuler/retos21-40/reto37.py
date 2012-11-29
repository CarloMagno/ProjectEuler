"""

"""
#import reto25
#import reto7

#def quitaDerecha(numero):
#	return numero/10
#	
#def quitaIzquierda(numero):
#	return numero%(10**(reto25.numDigitos(numero)-1))

#def trucantable(numero):
#	numIz = numero
#	numDe = numero
#	while numIz > 0 and numDe > 0:
#		if reto7.isPrime(numIz) and reto7.isPrime(numDe): 
#			numIz = quitaIzquierda(numIz)
#			numDe = quitaDerecha(numDe)
#		else:
#			return False
#	return True
#	
#	
#if __name__ == "__main__":
#	encontrados = 0
#	suma = 0
#	num = 113
#	while encontrados < 11:
#		if truncatable(num):
#			print num
#			suma += num
#			encontrados += 1
#		num += 2
#	print suma

from reto7 import isPrime
from math import log10
 
primes = [23,37,53,73,313,317,373,797,3137,3797,7937,31397,31973,37313,37397,71317,
71713,71917,73973,79397,313717,317197,319313,371737,371797,373717,373937,
379397,713737,713917,717317,717397,717917,719197,719713,719717,731713,
731737,739373,739397,791317,791797,793717,797917]
 
def trunc(n):
  c = n
  while c>10:
    c = c % 10**(int(log10(c)))
    n = n//10
    if not isPrime(c) or not isPrime(n): return False 
  return True
 
c = 0
s = 0
for p in primes:
  if trunc(p): 
    print p
    c += 1
    s += p
 
print c,"primos encontrados para una suma de",s
