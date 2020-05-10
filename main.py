import os
import logging
import numpy as np
import cv2
import traceback
from matplotlib import pyplot as plt
from pixel_manipulator import *
from utils import  *

logging.basicConfig(level=logging.DEBUG)


IMAGE_NAME = "frag_107.png"

def get_img_path(image_name):
    folder_path = os.getcwd()
    return folder_path + "\images\\fragments\\" + image_name

def verify_if_path_exists(path):
    return os.path.exists(path)


def print_pixels_values(opened_image):
    try:
        print(opened_image)
    except(Exception):
        logging.error("Are you sure this image is a numpy array?")
        traceback.print_exc()


def get_image_height(opened_image):
    height,width,color_levels = opened_image.shape
    return height

def get_image_width(opened_image):
    height,width,color_levels = opened_image.shape
    return width

def get_image_size(opened_image):
    height, width, color_levels = opened_image.shape
    size_dict = dict()
    size_dict['height'] = dict(height)
    size_dict['width'] = dict(width)
    return size_dict

def get_image_color_levels(opened_image):
    height,width,color_levels = opened_image.shape
    return color_levels

def get_percentage_of_black_pixels(opened_image):
    pixel_count = 0
    black_pixels_count = 0
    image = np.array(opened_image)
    image.flatten()


    for pixel in image:

        pixel_count += 1
        print(image[pixel])
        if (np.array_equal(image[pixel], [0, 0, 0])):
            black_pixels_count += 1

    return calculate_percentage(black_pixels_count, pixel_count + black_pixels_count)





def show_colors_histogram(colored_opened_image):
    color = ('b', 'g', 'r')

    for i, col in enumerate(color):
        histr = cv2.calcHist([colored_opened_image], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()





if __name__ == "__main__":
    fragment_image = cv2.imread(get_img_path(IMAGE_NAME), cv2.IMREAD_COLOR)


    print("The number of black pixel in the image is {}%".format(get_percentage_of_black_pixels(fragment_image)))

    # cv2.imshow('image', fragment_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



