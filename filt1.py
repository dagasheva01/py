from PIL import Image, ImageDraw
im = Image.open("carl.jpg")
rgb_im = im.convert("RGB")
size = rgb_im.size
h, w = size
pix = rgb_im.load()
colors = {}
for y in range(0, size[1]):
	for x in range(0, size[0]):
		r, g, b = pix[x, y]
		r = r // 5
		g = g // 5
		b = b // 5
		if r + g + b < 50:
			continue 
		if (r, g, b) in colors:
			colors[r, g, b] += 1
		else:
			colors[r, g, b] = 1
max_color = 0, 0, 0
max_value = 0
for k in colors:
	r, g, b = k
	value = colors[r, g, b]
	if value > max_value:
		max_color = (r, g, b)
		max_value = value

print(max_color)
for y in range(0, size[1]):
	for x in range(0, size[0]):
		r, g, b = pix[x, y]
		#s = (r + g + b) // 3
		r = min(r + max_color[0]*1 + 40, 255)
		g = min(g + max_color[1]*1 + 20, 255) 
		b = min(b + max_color[2]*1, 255)
		pix[x, y] = (r, g, b)

rgb_im.save("img_new.jpg")