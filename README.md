# Minecraft-To-Ascii

Converting regular Minecraft textures to Ascii

STATUS ON COMPLETION: 3/4 🥴

Here is a description of what all of the files do here:

| File | Description |
| ----- | ----- | 
| textures | All of the Minecraft 1.8.9 textures |
| texturesOutput | Where all the new textures go | 
| PressStart2P-Regular.ttf | This is the font that is used in main.py for writing the text from the original image to black_box.png |
| black_box.png | A 256 x 256 completely black box where the text is writen on to |
| main.py | Where all of the converting code is stored (see below for more) |
| findFilepaths.py | A program to get all of the filepaths from textures |
| filepaths.txt | Where all of those filepaths are stored |

# How this project works:

## Step 1 - find the filepaths:

Where does this step happen? findFilepaths.py & filepaths.txt & textures

Using the built-in os library in python, this program goes through the textures directory and gets every single filepath in the directory.

Then it writes all of the files that are pngs and aren't part of the textures/font sub-directory to filepaths.txt

Note: *This is a one time use file*

## Step 2 - convert images to text

**This part is not done yet**
Almost though.

## Step 3 - convert text back to images

**This part is not done yet**


