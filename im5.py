from PIL import Image, ImageDraw, ImageFont
text = "Salem"
color = (0, 0, 120)
img = Image.new('RGB', (150, 100), color)
fnt = ImageFont.truetype('Lobster/Lobster.otf', 40)
imgDrawer = ImageDraw.Draw(img)
imgDrawer.text((20, 20), text, font = fnt)
img.save("pil-example-05.png")