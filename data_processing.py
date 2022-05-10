"""
This file contains a python script to select all the images from the folder and resize them to 128X128
 and save them on a specific file.
"""

import os
import numpy as np
from PIL import Image


def img_proc(input_path, img_size, output_path):

    # Defining an image size and image channel
    # We are going to resize all our images to 128X128 size and since our images are colored images
    # We are setting our image channels to 3 (RGB)
    IMAGE_SIZE = img_size
    IMAGE_CHANNELS = 3

    # Defining image dir path.
    images_path = input_path

    training_data = []

    # Iterating over the images inside the directory and resizing them using Pillow's resize method.
    for filename in os.listdir(images_path):
        for file in os.listdir(images_path):
            prepath = os.path.join(images_path, filename)
            path = os.path.join(prepath, file)
            image = Image.open(path).resize((IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)

        training_data.append(np.asarray(image))

    training_data = np.reshape(
        training_data, (-1, IMAGE_SIZE, IMAGE_SIZE, IMAGE_CHANNELS))
    training_data = training_data / 127.5 - 1

    np.save('cubism_data.npy', training_data)