"""
Euler's Totient function, phi(n) [sometimes called the phi function], 
is used to determine the number of numbers less than n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are 
all less than nine and relatively prime to nine, phi(9)=6.

It can be seen that n=6 produces a maximum n/phi(n) for n  10.

Find the value of n  1,000,000 for which n/phi(n) is a maximum.
"""
from reto5 import mcd
from reto21 import divisoresPropios
from reto7 import isPrime
import math
import time

def factorization(k):
	s = 2
	fs = []
	fs = set(fs)
	for j in range(s, int(math.sqrt(k))+1):
		while k%j == 0:
			#fs.append(j)
			fs.add(j)
			k = k // j
	if (k != 1):
		fs.add(k)
	return list(fs)

def phi(n):
#	return len([i for i in range(1,n) if mcd(i,n)==1])
	if isPrime(n):
		return n-1
	else:
		prod = float(n)
		factores = factorization(n)
		for i in factores:
			prod = prod * (1 - (1/float(i)))
		return int(prod)

if __name__ == "__main__":
	maximo = 0.0
	res = 0
	start = time.time()
	for i in range(2,(10**6)+1):
		valor = i/float(phi(i))
		if valor > maximo:
			maximo = valor
			res = i
	print "Found!:",res
	finish = time.time()
	print finish-start,"sg"
#	for i in range(999990,10**6+1):
#		print i,":",i/float(phi(i))
