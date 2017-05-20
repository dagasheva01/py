s="())"
l=[]
ok=True
for c in s:
	if c == '(':
		l.append(c)
	elif c == ')':
		if len(l)>0:
			a=l.pop()
		else:
			ok= False
			break
if len(l) == 0 and ok:
	print("YES")
else:
	print("NO")