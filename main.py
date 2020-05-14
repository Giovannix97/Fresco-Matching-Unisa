import os
import logging
import cv2
from image_manipulator import *
from pixel_manipulator import *
import numpy as np #rimuovilo
from utils import *

logging.basicConfig(level=logging.DEBUG)

IMAGE_NAME = "frag_2.png"



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


def expand_image(image):

    LEFT_COLUMN_BOUND = 1
    RIGHT_COLUMN_BOUND = get_image_width(image) - 1

    TOP_ROW_BOUND = 1
    BOTTOM_ROW_BOUND = get_image_height(image) - 1

    PERMISSIBLE_PERCENTAGE_OF_BLACK = 30

    logging.info("RIGHT_COLUMN_BOUND: {}. BOTTOM_ROW_BOUND: {}".format(RIGHT_COLUMN_BOUND,BOTTOM_ROW_BOUND))

    for row in range(TOP_ROW_BOUND,BOTTOM_ROW_BOUND):
        for column in range(LEFT_COLUMN_BOUND,RIGHT_COLUMN_BOUND):
            if(get_percentage_of_black_neighbors(image,row,column) > PERMISSIBLE_PERCENTAGE_OF_BLACK):
                # I'm not in the centre of the fragment. I can be in the black zone or in the border.

                blue_values_neighbors = get_blue_neighbors_pixel_values(image,row,column)
                green_values_neighbors = get_green_neighbors_pixel_values(image,row,column)
                red_values_neighbors = get_red_neighbors_pixel_values(image,row,column)

                blue_average_value = calculate_int_average(blue_values_neighbors)
                green_average_value = calculate_int_average(green_values_neighbors)
                red_average_value = calculate_int_average(red_values_neighbors)
                change_pixel_color_and_return_image_BGR(image,row,column,blue_average_value,green_average_value,red_average_value)

            else:
                # Probably I'm in the centre of the fragment.
                pass


    return image

if __name__ == "__main__":
    fragment_image = cv2.imread(get_img_path(IMAGE_NAME), cv2.IMREAD_COLOR)

    for i in range (1,70):
       fragment_image = expand_image(fragment_image)
    cv2.imshow('image', fragment_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



