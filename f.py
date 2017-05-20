n=int(input())
s=1
s0=-1
for i in range(1, n+1):
	s += s0/(2.0*i+1)
	s0= -s0
print(4*s)