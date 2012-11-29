A = [[0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0]]

def ackermann(m,n):
	if m == 0:
		return n+1
	elif n == 0:
		return ackermann(m-1,1)
	else:
		return ackermann(m-1,ackermann(m,n-1))

def ackermannDP(m,n):
	if m == 0:
		return A[m][n]
	elif n == 0:
		return A[m-1][1]
	else:
		return A[m-1][A[m][n-1]]

#==============================================
#									MAIN
#==============================================
if __name__ == "__main__":			 
	for n in range(0,len(A)):
		A[0][n] = ackermann(0,n)
	
	for n in range(0,len(A)):
		A[1][n] = ackermann(1,n)

	for n in range(0,len(A)):
		A[2][n] = ackermann(2,n)
		
	for n in range(0,len(A)):
		A[3][n] = ackermann(3,n)
	
	print A
	
	for n in range(0,len(A)):
		A[4][n]	= ackermannDP(4,n)
	
	print A[4]
