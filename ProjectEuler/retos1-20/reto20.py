"""
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! 
is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(n):
	prod = 1
	prod = long(prod)
	
	for i in range(n+1):
		if i!=0:
			prod = prod * i

	return prod

def sumaDigitos(n):
	suma = 0
	while(n>9):
		suma += n%10
		n /= 10
	suma +=n
	return suma

if __name__ == "__main__":
	print sumaDigitos(factorial(100))
