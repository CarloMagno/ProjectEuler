#!/usr/bin/env python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

import reto7

def esPrimo(n):
	for i in range(n):
		if i!=0 and i!=1 and i!=2:
			if n%i==0:
				return False
	return True

if __name__ == "__main__":
	num = 600851475143L
	#lista = [long(i) for i in reversed(long(num)) if i!=0 and num%i==0 and esPrimo(i)]
	for i in reversed(range(long(math.sqrt(num)))):
		if num % i == 0 and reto7.isPrime(i):
			lista = i
			break

	print lista
