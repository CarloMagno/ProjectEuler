"""
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are
 an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def divisoresPropios(n):
	lista=[]
	for i in range(1,(n/2)+1):
		if (n%i)==0:
			lista.append(i)
	return lista

def sonAmigos(a,b):
	return a == sum(divisoresPropios(b)) and b == sum(divisoresPropios(a))

if __name__ == "__main__":
	listaSumaDivisores = []
	suma = 0
	amigos = []
	for i in range(0,10000):
		listaSumaDivisores.append(sum(divisoresPropios(i)))

	for i in range(0,10000):
			a = listaSumaDivisores[i]
			if a < 10000:
				b = listaSumaDivisores[a]
				if b < 10000:
					j = listaSumaDivisores.index(b)
					if i == b and a != b:
						suma = suma + i
						amigos.append([i,j])
						print "Amigos:",i,"&",j
	print amigos
	print suma
#	suma = 0
#	for i in range(0,10000):
#		j = sum(divisoresPropios(i))
#		k = sum(divisoresPropios(j))
#		if i == k and j != k:
#			print "Amigos:",i,"&",j
#			suma += j
#	print suma
