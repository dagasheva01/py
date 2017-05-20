s=str(input())
index1=0
index2=0
for i in range(0, len(s)):
	if s[i]=="h":
		index1=i
		break
for i in range (len(s)-1, index1, -1):
	if s[i]=="h":
		index2=i+1
		break
print(s[:index1]+s[index2:])