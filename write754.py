import PIL
from PIL import ImageFont, Image, ImageDraw

im = Image.open('A754_igu.eps').convert('RGBA')

x, y =  im.size
eX, eY = 188, 188 #Size of Bounding Box for circle

bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
draw = ImageDraw.Draw(im)
draw.ellipse(bbox, outline = 'white')

#eXb, eYb = 12,12    #Size of Bounding Box for circle

#bboxb =  (x/2 - eXb/2, y/2 - eYb/2, x/2 + eXb/2, y/2 + eYb/2)
#drawb = ImageDraw.Draw(im)
#drawb.ellipse(bboxb, fill=0)
#del drawb

txt = Image.new('RGBA', im.size, (255,255,255,0))
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 18)

d = ImageDraw.Draw(txt)

d.text((410,20), "Cluster: A754", font=fnt, fill=(255,255,255,255))
d.text((390,50), "Redshift = 0.054", font=fnt, fill=(255,255,255,255))
d.text((320,80), "Einstein radius: 17.43\"", font=fnt, fill=(255,255,255,255))

d.text((250,550), "10 kpc", font=fnt, fill=(255,255,255,255))

draw.line([(260,540),(308.18,540)], fill=(255,255,255,255), width=3)
del draw
im = Image.alpha_composite(im, txt)
im.save("cA754_galfit.jpg")
#im.show()
