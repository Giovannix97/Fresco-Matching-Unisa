import os
import logging
import cv2
from image_manipulator import *
from pixel_manipulator import *
import numpy as np
from utils import *

logging.basicConfig(level=logging.DEBUG)

IMAGE_NAME = "frag_457.png"



def get_img_path(image_name):
    """
    Get the path of the folder in which are stored all the fragments

    :param image_name:
    :return: A string that represents the image path.
    """
    folder_path = os.getcwd()
    return folder_path + "\images\\fragments\\" + image_name


def verify_if_path_exists(path):
    """
    Verify if the image/folder exists.

    :param path:
    :return: True if the path exists.
    """
    return os.path.exists(path)


def expand_image(image,iteration):

    LEFT_COLUMN_BOUND = 1
    RIGHT_COLUMN_BOUND = get_image_width(image) - 1

    TOP_ROW_BOUND = 1
    BOTTOM_ROW_BOUND = get_image_height(image) - 1

    IMAGE_CENTER_X = int(get_image_width(image)/2)
    IMAGE_CENTER_Y = int(get_image_height(image)/2)

    MINIMUM_PERCENTAGE_OF_BLACK = 25
    MAXIMUM_PERCETANGE_OF_BLACK = 80
    logging.info("RIGHT_COLUMN_BOUND: {}. BOTTOM_ROW_BOUND: {}".format(RIGHT_COLUMN_BOUND,BOTTOM_ROW_BOUND))

    
    for row in range(TOP_ROW_BOUND,IMAGE_CENTER_X):
        for column in range(RIGHT_COLUMN_BOUND,IMAGE_CENTER_Y):
            if (is_image_pixel_black(image, row, column)):
                black_neigh_percent = get_percentage_of_black_neighbors(image, row, column)
                if (black_neigh_percent > MINIMUM_PERCENTAGE_OF_BLACK) and (black_neigh_percent < MAXIMUM_PERCETANGE_OF_BLACK):
                    neighbors_color_values = get_neighbors_pixels_colors(image, row, column)
                    for neighbor_value in neighbors_color_values:
                        if (is_pixel_black(neighbor_value)):
                            pass
                        else:
                            image = change_pixel_color_and_return_image_BGR(image, row, column,
                                                                            get_blue_value_of_a_pixel(neighbor_value),
                                                                            get_green_value_of_a_pixel(neighbor_value),
                                                                            get_red_value_of_a_pixel(neighbor_value))
    for row in range(BOTTOM_ROW_BOUND,IMAGE_CENTER_X):
        for column in range(LEFT_COLUMN_BOUND,IMAGE_CENTER_Y):
            if (is_image_pixel_black(image, row, column)):
                black_neigh_percent = get_percentage_of_black_neighbors(image, row, column)
                if (black_neigh_percent > MINIMUM_PERCENTAGE_OF_BLACK) and (black_neigh_percent < MAXIMUM_PERCETANGE_OF_BLACK):
                    neighbors_color_values = get_neighbors_pixels_colors(image, row, column)
                    for neighbor_value in neighbors_color_values:
                        if (is_pixel_black(neighbor_value)):
                            pass
                        else:
                            image = change_pixel_color_and_return_image_BGR(image, row, column,
                                                                            get_blue_value_of_a_pixel(neighbor_value),
                                                                            get_green_value_of_a_pixel(neighbor_value),
                                                                            get_red_value_of_a_pixel(neighbor_value))
    for row in range(BOTTOM_ROW_BOUND,IMAGE_CENTER_X):
        for column in range(RIGHT_COLUMN_BOUND,IMAGE_CENTER_Y):
            if (is_image_pixel_black(image, row, column)):
                black_neigh_percent = get_percentage_of_black_neighbors(image, row, column)
                if (black_neigh_percent > MINIMUM_PERCENTAGE_OF_BLACK) and (black_neigh_percent < MAXIMUM_PERCETANGE_OF_BLACK):
                    neighbors_color_values = get_neighbors_pixels_colors(image, row, column)
                    for neighbor_value in neighbors_color_values:
                        if (is_pixel_black(neighbor_value)):
                            pass
                        else:
                            image = change_pixel_color_and_return_image_BGR(image, row, column,
                                                                            get_blue_value_of_a_pixel(neighbor_value),
                                                                            get_green_value_of_a_pixel(neighbor_value),
                                                                            get_red_value_of_a_pixel(neighbor_value))




    return image


if __name__ == "__main__":
    fragment_image = cv2.imread(get_img_path(IMAGE_NAME), cv2.IMREAD_COLOR)

    for i in range (1,5):
      fragment_image = expand_image(fragment_image,i)


    cv2.imshow('image', fragment_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



