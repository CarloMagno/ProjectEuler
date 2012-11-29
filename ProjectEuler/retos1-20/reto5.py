
"""
2520 is the smallest number that can be divided by each of 
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?
"""

def mcd(a,b):
	a, b = max(a,b), min(a,b)	
	while b>0:
		a,b = b,a%b
	return a

def mcm(a,b):
	return a*b/mcd(a,b)

if __name__ == "__main__":
	print reduce(mcm, range(1,21))
