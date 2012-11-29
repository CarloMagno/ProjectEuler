import math

def pentagonal(n):
	return n*(3*n-1)/2

def esPentagonal(x):
	n = (math.sqrt(24*x+1)+1)/6
	return n.is_integer()

if __name__ == "__main__":
	minimo = 1000000000000L
	for a in range(1,2500):
		j = pentagonal(a)
		for b in range(1,2500):
			k = pentagonal(b)
			suma = j+k
			dif = abs(j-k)
			if esPentagonal(suma) and esPentagonal(dif):
				if minimo > dif:
					minimo = dif
	print minimo
#	Lpent = [pentagonal(i) for i in range(998,2000)]
#	print "Lista generada"
##	print Lpent.index()
#	for j in Lpent:
#		for k in Lpent:
#			suma = j+k
#			dif = abs(j-k)
#			if Lpent.count(suma) > 0:
##				print j,"+",k,"=",suma
#				if Lpent.count(dif) > 0:
##					print "DIF=",dif
#					if minimo > dif:
#						minimo = dif
#	print "Found!:",minimo
