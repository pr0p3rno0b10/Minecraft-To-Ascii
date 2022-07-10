from PIL import Image, ImageDraw, ImageFont

def resize_image(image, new_width = 32):
	width, height = image.size
	ratio = height / width
	new_height = int(new_width * ratio)
	resized_image = image.resize((new_width, new_height))
	return resized_image

def grayify(image):
	grayscale_image = image.convert("L")
	return grayscale_image

def pixels_to_ascii(image):
	ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return characters

#def generateNewFilepath(path):


def main(path, new_width = 32):
	# test path
	
	image = Image.open(path)

	new_image_data = pixels_to_ascii(grayify(resize_image(image)))
	
	pixel_count = len(new_image_data)
	ascii_image = "\n".join(new_image_data[i:i + new_width] for i in range(0, pixel_count, new_width))

	with open("test_ascii_image.txt", "w") as f:
		f.write(ascii_image)

	font = ImageFont.truetype("PressStart2P-Regular.ttf", 8)
	
	black_box_filepath = "black_box.png"
	black_box = Image.open(black_box_filepath)
	# resized_black_box = black_box.resize((round(black_box.size[0] * 37.45), round(black_box.size[1] * 35.7)))

	draw = ImageDraw.Draw(black_box)

	draw.text((0, 0), ascii_image, fill = (255, 255, 255), font = font)
	
	black_box.save("test.png")

with open("filepaths.txt", "r") as f:
	filepaths = f.readlines()

'''
for filepath in filepaths:
	img = Image.open(filepath)
	width = img.size[0]
	main(filepath, width*2)
'''
filepath = "textures/blocks/tallgrass.png"
img = Image.open(filepath)
width = img.size[0]
main(filepath, width*2)







