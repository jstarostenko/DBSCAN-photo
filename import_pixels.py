from PIL import Image
import numpy as np

def imp_pixels(file_name):
	def create_pixel_array(file_name):
		with open(file_name) as f: #when this is closed, image is closed
			image = Image.open(f)
			return np.array(image, dtype = np.float64)

	pixel_array = create_pixel_array(file_name)

	a = []
	for i in pixel_array:
		for j in i:
			a.append(j)

	return a		