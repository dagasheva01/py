word1=input()
for i in range(0,len(word1)):
	if word1[i]=='h':
		index1=i
		break
for i in range(len(word1)-1,index1, -1):
	if word1[i]=='h':
		index2=i
		break
word2=word1[index2:index1:-1]
print(word1[:index1]+word2+word1[index2:])