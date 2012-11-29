#!/usr/bin/env python
"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

#tams = range(0,10**6)

#def calculaTam(n):
#	tam = 1
#	prim = n
#	fin = False
#	#print "CalculaTam de",n
#	while fin == False and n!=1:
#		#print "Tams[n-1]=",tams[n-1]
#		if tams[n-1] == 0:
#			if n%2==0:
#				#print "par",n
#				n /= 2	
#			else:
#				#print "impar",n
#				n = n*3+1		
#			tam += 1
#		else:
#			tam += tams[n-1]
#			fin = True
#	
#	#tams[prim-1] = tam
#	print "En posicion", prim-1, "tamanyo de", prim, "=", tam
#	return tam

#if __name__ == "__main__":

#	for i in range(0,10**6):
#		tams[i] = 0
#	
#	for i in range(0,10**6):
#		tams[i] = calculaTam(i+1)
#		print tams[i]
#		
##	print tams[0:20]
#	print max(tams)

def calculaTam(n):
	tam = 1
	prim = n
	fin = False
	while fin == False and n!=1:
		if n%2==0:
			n /= 2	
		else:
			n = n*3+1		
		tam += 1
	return tam


if __name__ == "__main__":
		tamMaximo = 0
		maximo = 1
		for i in range(1,10**6+1):
			tam = calculaTam(i)
			if tamMaximo < tam:
				tamMaximo = tam
				maximo = i
		print maximo

