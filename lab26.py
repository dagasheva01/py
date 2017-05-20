a=input()
n=0
b=-2
for i in range(0, len(a)):
	if a[i]=="f":
		n=n+1
		b=-1
		if n==2:
			b=i
print(b)