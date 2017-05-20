import sys; from PIL import Image;

chars = list(' .oxX#$')

f, scale, GCF, WCF = sys.argv[1], 0.25, 1, 7/4

img = Image.open(f).convert("L")
size = ( round(img.size[0]*scale*WCF), round(img.size[1]*scale) )
img = img.resize(size)
minig = img.getpixel((0, 0))
maxig = img.getpixel((0, 0))


for y in range(0, size[1]):
	for x in range(0, size[0]):
		g = img.getpixel((x, y))
		if g < minig:
			minig = g
		if g >  maxig:
			maxig = g

maxig = maxig - minig

for y in range(0, size[1]):
	for x in range(0, size[0]):
		g = img.getpixel((x, y))
		g = g - minig
		i = int((1.0 - g/maxig)*(len(chars) - 1))
		print(chars[i], end ="")
	print("\n", end = "")