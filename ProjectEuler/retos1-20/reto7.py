#!/usr/bin/env python
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10001st prime number?
"""
import math
def esPrimo(n):
	for i in range(n):
		if i!=0 and i!=1 and i!=2:
			if n%i==0:
				return False
	return True

def redondear(n):
	pass

def isPrime(n):
	if n == 1:
		return True
	elif n < 4:
		return True
	elif n%2 == 0:
		return False
	elif n < 9:
		return True
	elif n%3 == 0:
		return False
	else:
		r = int(math.sqrt(n))+1
		f = 5
		while f <= r:
			if n%f == 0:
				return False
			if n%(f+2) == 0:
				return False
			f = f+6
		return True

if __name__ == "__main__":
	num = 0
	i = 1
	while num<10001:
		if isPrime(i):
			num+=1
			print num,i
		i+=2
	
#	print [i for i in range(100) if esPrimo(i) and i!=0]
	
#	print [i for i in range(100) if isPrime(i) and i!=0]
