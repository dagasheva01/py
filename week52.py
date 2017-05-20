s= input()
s= s.split(" ")
l=[]
for c in s:
	if c.isnumeric():
		l.append(c)
	else:
		if len(l) < 2:
			ok= False
			break
		else:
			b= l.pop()
			a= l.pop()
			k=0
			if c == "+":
				k=int(a)+int(b)
			elif c == "-":
				k=int(a) - int(b)
			elif c == "*":
				k=int(a)*int(b)
			l.append(k)
print(l)