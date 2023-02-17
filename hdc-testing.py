import numpy as np
from scipy.spatial.distance import hamming
from test import encode_image_as_binary
from PIL import Image

image1 = Image.open("Images/1.jpg")
image2 = Image.open("Images/2.jpg")
image3 = Image.open("Images/3.jpg")
image4 = Image.open("Images/4.jpg")

image1 = image1.resize((256,256))
image2 = image2.resize((256,256))
image3 = image3.resize((256,256))
image4 = image4.resize((256,256))

hv_1 = list(encode_image_as_binary(10000,image1))
hv_2 = list(encode_image_as_binary(10000,image2))
hv_3 = list(encode_image_as_binary(10000,image3))
hv_4 = list(encode_image_as_binary(10000,image4))

# hv generation
def gen_hv(seed,D=10000):
    rng = np.random.default_rng(seed)
    hv = rng.choice([0, 1], size=D).astype(np.int16)
    return hv

#item memory
def gen_im(seed,D=10000,N=2):
    rng = np.random.default_rng(seed)
    im = []
    for n in range(N):
        im.append(gen_hv(rng,D))
    im = np.vstack(im)
    return im
item_memory = gen_im(1)

print(len(item_memory))
print(hamming(item_memory[0],item_memory[1]))
print(len(hv_1))
print(len(hv_2))
print(len(hv_3))
print(len(hv_4))
print(hamming(hv_1,hv_2))
print(hamming(hv_2,hv_3))
print(hamming(hv_3,hv_1))
print(hamming(hv_4,hv_3))
print(hamming(hv_4,hv_2))
print(hamming(hv_4,hv_1))
