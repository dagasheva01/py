a, b, c= [int(input()) for i in range(3)]
if ((a+b)>c and (a+c)>b and (b+c)>a):
	print("YES")
else:
	print("NO")