import sys
from PIL import Image

def instagram_look(image_file, count=0):
	images = map(Image.open, ['instagram_above.jpg', image_file, 'instagram_below.jpg'])
	widths, heights = zip(*(i.size for i in images))

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in images:
	  new_im.paste(im, (x_offset,0))
	  x_offset += im.size[0]

	return new_im




def resize_image(image_file):
	basewidth = 300 # figure out insta width
	img = Image.open(image_file)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
	# img.save('sompic.jpg')
	return img






# get all images in folder...
image_files = ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']


# calc c based on old instas
c = 0
for i in image_files:
	r = resize_image(i)
	insta = instagram_look(r, c)
	n = 'instagram_{}.jpg'.format(count)
	insta.save(n)
	# > open(n)
	# mv i > old/i
	c += 1