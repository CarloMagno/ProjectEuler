
def sumaDigPow5(n):
	suma = 0
	while n > 9:
		suma += (n%10)**5
		n = n/10
	suma += n**5
	return suma

if __name__ == "__main__":
	sumaFinal = 0
	num = 10
	fin = False
	while not fin:
		print num
		suma = sumaDigPow5(num)
		if suma == num:
			sumaFinal += num
		if 2*10**5 < num:
			fin = True
		num += 1
	print sumaFinal
