from PIL import Image, ImageDraw, ImageFont
color = (0, 0, 120)
img = Image.open("carl.jpg")
font = ImageFont.truetype('Lobster/Lobster.otf', 40)
size = img.size
imgDrawer = ImageDraw.Draw(img)
text = "У меня 29 по Programming Technologies"
h, w = size
bound_w = w - 200
width, height = font.getsize(text)
y = 20
if width > bound_w:
	k = width // bound_w
	k = k  + 1
	words = text.split(" ")
	n = len(words)
	p = n // k
	new_txt = []
	for i in range(0, k):
		new_txt = " ".join(words[i*p:(i+1)*p])
		imgDrawer.text((100, y), new_txt, font = font)
		y = y + height


text = "По Programming Technologies, Карл!!"
h, w = size
bound_w = w - 200
width, height = font.getsize(text)
y = h - 100
if width > bound_w:
	k = width // bound_w
	k = k  + 1
	words = text.split(" ")
	n = len(words)
	p = n // k
	new_txt = []
	for i in range(0, k):
		new_txt = " ".join(words[i*p:(i+1)*p])
		imgDrawer.text((100, y), new_txt, font = font)
		y = y + height

img.save("pil-example-07.png")