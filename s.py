import io
import sys

in_file = open("input.txt", "r")
out_file = open("output.txt", "w")
# w = write (overwrite, create)
# a = append (not create)
# r = read
lines = in_file.readlines()

l = []
for line in lines:
	l.append(line.replace("\n", ""))

for line in l:
	out_file.write(line.upper()+"\n")