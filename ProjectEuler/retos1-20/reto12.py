import math
def cuentaFactores(n):
	factores = 0
	lim = int(math.sqrt(n)+1)
	for i in range(1,lim):
		if (n%i) == 0:
			factores += 2
	return factores

if __name__ == "__main__":
	numFactores = 0
	iter = 1
	tam = 1
	while numFactores <= 500:
		numFactores = cuentaFactores(tam)
		iter+=1
		tam += iter
		print tam
	print "Found:",tam-iter
