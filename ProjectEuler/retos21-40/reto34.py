"""
145 = 1! + 4! + 5! = 1 + 24 + 120 = 145
Find the sum of all numbers which are equal to the sum of the factorial
of their digits.
1!=1 and 2!=2 are not sums they are not included
"""

from reto15 import factorial

def sumaDigFact(n):
	suma = 0
	while n > 9:
		suma += factorial(n%10)
		n = n/10
	suma += factorial(n)
	return suma

if __name__ == "__main__":
	sumaFinal = 0
	num = 10
	fin = False
	while not fin:
		print num
		suma = sumaDigFact(num)
		if suma == num:
			sumaFinal += num
		if 2*10**5 < num:
			fin = True
		num += 1
	print sumaFinal
