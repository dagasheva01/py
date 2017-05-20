# palindrome
# anagram
s = "Hello, my name is Dauren 12425."
s = s.upper()
s = s.lower()
l = s.split()
first_word = l[0]
last_word = l[-1]
print(first_word)
print(last_word)
s = s.replace(",", "")
ll = []
for c in s:
	if c.isalpha() or c == ' ':
		ll.append(c)
s = "".join(ll)
print(s)

s1 = 'Dauren'
s2 = 'Neruad'
s1 = s1.lower()
s2 = s2.lower()
if len(s1) == len(s2):
	l1 = []
	l2 = []
	for c in s1:
		l1.append(c)
	for c in s2:
		l2.append(c)
	l1 = sorted(l1)
	l2 = sorted(l2)
	ok = True
	for i in range(0, len(l1), 1):
		if l1[i] != l2[i]:
			ok = False
			break
	print(ok)


