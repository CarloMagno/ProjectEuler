"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
"""
import reto4

def base2(num):
	if num <= 1:
		return num
	else:
		return base2(num/2)*10 + num%2
		

if __name__ == "__main__":
	suma = 0
	for i in range(1,10**6):
		if reto4.capicuo(i) and reto4.capicuo(base2(i)):
			suma += i
	print suma

