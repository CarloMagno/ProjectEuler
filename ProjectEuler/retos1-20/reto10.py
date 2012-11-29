"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import reto7

if __name__ == "__main__":
	print sum([long(i) for i in range(2*(10**6)) if reto7.isPrime(i) and i>1])
