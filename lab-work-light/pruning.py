from PIL import Image

name = 'yellow_nk'

im = Image.open('photos/{nm}.jpg'.format(nm = name))
im = im.crop((890, 430, 1205, 650)).rotate(180)
im.save('pruningphotos/{nm}.jpg'.format(nm = name))
im.show()