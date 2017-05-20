import re
x=input()
p=re.compile("^\d\d[0][1-9]|(10|11|12)[1-31]\d\d\d \d\d\d$")
if p.match(str(x)) is not None:
	print("YES")
else:
	print("NO")