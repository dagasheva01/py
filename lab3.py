import re
x=input()
p=re.compile("^\+7\(727\)\d\d\d \d\d\d\d$")
if p.match(str(x)) is not None:
	print("YES")
else:
	print("NO")
