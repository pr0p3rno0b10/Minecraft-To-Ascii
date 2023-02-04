from PIL import Image
import os

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
	#ASCII_CHARS = [" ", ".", ":", ";", "+", "^", "?", "%", "S", "@", "#"]
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return characters

def modifyImage(image):
	grayifiedImage = grayify(image)
	pixelatedImage = pixels_to_ascii(grayifiedImage)
	return pixelatedImage

def createNewFilepath(path):
  newFilePath = "texturesOutput/"
  splitPath = path.split("/")
  splitPath.remove("textures")

  ending = ""
  
  for filePart in splitPath:
    if filePart.endswith(".png"):
      ending = filePart
    else:
      newFilePath += filePart + "/"

  return [newFilePath, ending]

def convertImageToAscii(filepath):
	image = Image.open(filepath)
	modifiedImage = modifyImage(image)

	width, height = image.size

	newWidth = width * 7
	newHeight = height * 7

	newImage = Image.new(mode="RGB", size=(newWidth, newHeight))

	x = 0
	y = 0
	for char in modifiedImage:
		upscaledChar = getQuad(char)

		newImage.paste(upscaledChar, (x, y))
		x += 7
		if x == newWidth:
			x = 0
			y += 7
	#newImage.show()

	filepathDetails = createNewFilepath(filepath)
	print(filepathDetails)
	newFilepathBeginning = filepathDetails[0]
	newFilepathEnding = filepathDetails[1]

	if not os.path.exists(newFilepathBeginning):
		os.makedirs(newFilepathBeginning)

	newImage.save(newFilepathBeginning + newFilepathEnding)




with open("filepaths.txt", "r") as f:
	allFilePaths = f.readlines()
	modifiedAllFilePaths = []

	for filepath in allFilePaths:
		modifiedAllFilePaths.append(filepath.rstrip())

for filepath in modifiedAllFilePaths:
	 convertImageToAscii(filepath)

