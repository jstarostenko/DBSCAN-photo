from PIL import Image
import numpy as np

def imp_pixels(filename):
    def create_pixel_array(filename):
        with open(filename) as f:
            image = Image.open(f)
            return np.array(image, dtype = np.float64)

    pixel_array = create_pixel_array(filename)

    a = []
    for i in pixel_array:
        for j in i:
            a.append(j)

    return a