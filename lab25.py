s=str(input())
n=s.find("f")
m=s.rfind("f")
if n==-1:
	pass
elif n==m:
	print(n)
else:
	print(n, m)