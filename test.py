import numpy as np
from scipy.spatial.distance import hamming
from PIL import Image
from scipy.fftpack import idct

def encode_image_as_binary(string_length,img):
    width, height = img.size
    binary_string = ""
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x,y))
            binary_string += "{0:b}".format(pixel[0]).zfill(8)
            binary_string += "{0:b}".format(pixel[1]).zfill(8)
            binary_string += "{0:b}".format(pixel[2]).zfill(8)
    return binary_string[:string_length]

