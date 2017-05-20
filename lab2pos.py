s = input()
j = 0
res=""
for i in range(0,len(s)-j):
	if s[i] != '@':
		res+=s[i]
print(res)