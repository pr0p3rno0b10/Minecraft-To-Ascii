from PIL import Image

def getQuad(character):
	asciiCharactersToCoords = {" ": (161, 1, 167, 7), "#": (1, 1, 7, 7), "@": (17, 1, 23, 7), "S": (33, 1, 39, 7), "%": (49, 1, 55, 7), "?": (65, 1, 71, 7), "^": (81, 1, 87, 7), "+": (97, 1, 103, 7), ";": (113, 1, 119, 7), ":": (129, 1, 135, 7), ".": (145, 1, 151, 7)}

	font = Image.open("font.png")

	for char in asciiCharactersToCoords:
		if char == character:
			quad = font.crop(asciiCharactersToCoords[char])

	return quad



def grayify(image):
	grayscale_image = image.convert("L")
	return grayscale_image

def pixels_to_ascii(image):
	ASCII_CHARS = [" ", "#", "@", "S", "%", "?", "^", "+", ";", ":", "."]
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return characters

def generateNewFilepath(path):
	newFilePath = "texturesOutput/"
	splitPath = path.split("/")

	for filePart in splitPath:
		if filePart.endswith(".png"):
			newFilePath += filepath
		else:
			newFilePath += filePart + "/"

	return newFilePath

def resize_image(image, new_width = 32):
	width, height = image.size
	ratio = height / width
	new_height = int(new_width * ratio)
	resized_image = image.resize((new_width, new_height))
	return resized_image


def main(path, new_width, new_height, newPath):
	image = Image.open(path)

	black_box_filepath = "black_box.png"
	black_box = Image.open(black_box_filepath)

	black_box = black_box.resize((new_width, height))

	new_image_data = pixels_to_ascii(grayify(image))
	
	pixel_count = len(new_image_data)
	ascii_image = "\n".join(new_image_data[i:i + new_width] for i in range(0, pixel_count, new_width))

	with open("test_ascii_image.txt", "w") as f:
		f.write(ascii_image)


	# draw.text((0, 0), ascii_image, fill = (255, 255, 255), font = font)
	
	x = 0
	y = 0
	for char in new_image_data:
		print("hi")
		image = getQuad(char)
		imageX, imageY = image.size
		black_box.paste(image, (x, y))
		if x == new_width:
			y += 7
			x = 0
		
		x += 7
	


	black_box.save(newPath)


	
	# resized_black_box.save("test.png")

	'''
	
	'''

with open("filepaths.txt", "r") as f:
	filepaths = f.readlines()


#for filepath in filepaths:
#	img = Image.open(filepath)
	
filepath = "textures/painting/paintings_kristoffer_zetterstrand.png"
newFilePath = generateNewFilepath(filepath)

img = Image.open(filepath)
width = img.size[1]
height = img.size[0]
main(filepath, width*7, height*7, newFilePath)







