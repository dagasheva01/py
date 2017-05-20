from PIL import Image, ImageDraw, ImageFont
text = "S"
color = (0, 0, 120)
img = Image.new('RGB', (10, 10), color)
imgDrawer = ImageDraw.Draw(img)
imgDrawer.text((2, -2), text)
img.save("pil-example-01.png")