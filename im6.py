from PIL import Image, ImageDraw, ImageFont
color = (0, 0, 120)
img = Image.open("black-guy-pointing.jpg")
fnt = ImageFont.truetype('Lobster/Lobster.otf', 20)
size = img.size
imgDrawer = ImageDraw.Draw(img)
text = "Нельзя обойти систему безопасности"
imgDrawer.text((20, 20), text, font = fnt)
text = "Если ее нет"
imgDrawer.text((20, size[0]-80), text, font = fnt)
img.save("pil-example-06.png")