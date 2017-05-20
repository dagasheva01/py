lol= input()
don=[]
non=[]
doit=-10
lll=-11
rrr=-12
emmm= -100
def precedence(a):
	if a is '+' or '-':
		return 1
	elif a is '*' :
		return 2
	else:
		return 99
def typeof(a):
	if a is '(':
		return lll
	elif a is ')':
		return rrr
	elif a is '+' or '-' or '*':
		return doit
	else:
		return crush
for i in lol:
	type= typeof(i)
	if type is lll:
