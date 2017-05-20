s=input()
l=[]
ok=True
for c in s:
	if c == '(' or c == '{' or c == '[' :
		l.append(c)
	elif c == ')' or c == '}' or c == ']':
		if len(l)>0:
			a=l.pop()
			if a == '(' and c != ')':
				ok= False
				break
			elif a == '{' and c != '}':
				ok= False
				break
			elif a == '[' and c != ']':
				ok = False
				break
		else:
			ok= False
			break
if len(l) == 0 and ok ==  True:
	print("yes")
else:
	print("no")