# one time use file
# just used to get all filepaths
import os

filepaths = []
for (dir_path, dir_names, file_names) in os.walk("textures/"):
  for file_name in file_names:
  	filepaths.append(os.path.join(dir_path, file_name))


with open("filepaths.txt", "w") as f:
	for filepath in filepaths:
		if filepath.endswith(".png") and not filepath.startswith("textures/font/"):
			f.write(filepath + "\n")

# there is a space at the end of the file