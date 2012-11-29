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

def isPermutation(n,k):

	n = str(n)
	k = str(k)
	if len(n)!=len(k):
		return False
	else:
		for i in range(len(n)):
			if k.find(n(i)) == -1:
				return False
		return True
	
if __name__ == "__main__":
	minimo = 1000000.0
	res = 0
	start = time.time()
	for i in range(2,10**7):
		print i
		valor = i/float(phi(i))
		if isPermutation(valor,i):
			if valor < minimo:
				minimo = valor
				res = i
	print "Found!:",res
	finish = time.time()
	print finish-start,"sg"
#	for i in range(999990,10**6+1):
#		print i,":",i/float(phi(i))
