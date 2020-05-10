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


def get_image_size(opened_image):
    height, width, color_levels = opened_image.shape
    size_dict = dict()
    size_dict['height'] = dict(height)
    size_dict['width'] = dict(width)
    return size_dict


def get_image_height(opened_image):
    height,width,color_levels = opened_image.shape
    return height


def get_image_width(opened_image):
    height,width,color_levels = opened_image.shape
    return width


def get_image_color_levels(opened_image):
    height,width,color_levels = opened_image.shape
    return color_levels




def rotate_image(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    # Perform the rotation
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated


def get_percentage_of_black_pixels(opened_image):
    # TODO
    # This method must be implemented
    pass

    #return calculate_percentage(black_pixels_count, pixel_count + black_pixels_count)


def get_percentage_of_white_pixels(opened_image):
    # TODO
    # This method must be implemented
    pass

    # return calculate_percentage(white_pixels_count, pixel_count + white_pixels_count)


def show_colors_histogram(colored_opened_image):
    color = ('b', 'g', 'r')

    for i, col in enumerate(color):
        histr = cv2.calcHist([colored_opened_image], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()




if __name__ == "__main__":
    fragment_image = cv2.imread(get_img_path(IMAGE_NAME), cv2.IMREAD_COLOR)

    cv2.imshow('image', fragment_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



