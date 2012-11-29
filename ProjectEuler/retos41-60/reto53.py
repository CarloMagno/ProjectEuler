"""
How manu, not necessarily distinct, values of nCr for 1 <= n <= 100
are greater than one-million?
"""
from reto15 import combinatorio
import time

if __name__ == "__main__":
	cont = 0
	res = 0
	res = long(res)
	start = time.time()
	for n in range(1,101):
		for r in range(1,n+1):
			res = long(combinatorio(n,r))
			if res > 10**6:
				cont += 1
	finish = time.time()
	print "Tiempo:",finish-start,"sg"
	print cont
