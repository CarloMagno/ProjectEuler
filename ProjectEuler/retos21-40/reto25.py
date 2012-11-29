"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def numDigitos(n):
	digitos = 1
	while (n > 9):
		digitos += 1
		n = n/10
	return digitos

if __name__ == "__main__":
	prim = 1
	seg = 1
	terc = prim+seg
	termino = 3
	while numDigitos(terc)<1000:
		termino += 1
		prim = seg
		seg = terc
		terc = prim+seg
	print termino
