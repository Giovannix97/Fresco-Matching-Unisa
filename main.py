import os
import logging
import numpy as np
import cv2


logging.basicConfig(level=logging.DEBUG)


IMAGE_NAME = "frag_30.png"

def get_img_path(image_name):
    folder_path = os.getcwd()
    return folder_path + "\images\\fragments\\" + image_name

def verify_if_path_exists(path):
    return os.path.exists(path)

def get_image(image_name):
    if not (verify_if_path_exists(get_img_path(image_name))):
        logging.error("Image not found! Please specify a correct name.")
    else:
        logging.info("Image opened")

def print_pixels_values(opened_image):
    try:
        print(opened_image)
    except(Exception):
        logging.error("Are you sure this image is a numpy array?")


def get_image_height(opened_image):
    height,width,color_levels = opened_image.shape
    return height

def get_image_width(opened_image):
    height,width,color_levels = opened_image.shape
    return width

def get_image_color_levels(opened_image):
    height,width,color_levels = opened_image.shape
    return color_levels

if __name__ == "__main__":
    print("Ciao")
    get_image(IMAGE_NAME)

    fragment_image = cv2.imread(get_img_path(IMAGE_NAME),cv2.IMREAD_COLOR)
    print_pixels_values(fragment_image)
    # print(get_image_color_levels(fragment_image))
    #
    # cv2.imshow('image', fragment_image)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

