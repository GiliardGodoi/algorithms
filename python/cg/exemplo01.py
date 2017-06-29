from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter

img = Image.open('img01.jpg')

img = ImageOps.autocontrast(img)
img = ImageOps.equalize(img)

img = img.filter(ImageFilter.CONTOUR)

img.thumbnail((512,512), Image.ANTIALIAS)

img = ImageOps.expand(img,border=2, fill=1)

img.save('tr03.png', 'PNG')