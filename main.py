import os
import logging
import cv2
from image_manipulator import *
from pixel_manipulator import *
import numpy as np
from utils import *

logging.basicConfig(level=logging.DEBUG)

IMAGE_NAME = "frag_56.png"


def get_img_path(image_name):
    """
    Get the path of the chosen fragment.

    :param image_name:
    :return: A string that represents the image path.
    """
    folder_path = os.getcwd()
    return folder_path + "\images\\fragments\\" + image_name


def get_folder_path():
    """
        Get the path of the folder in which are stored all the fragments

        :return: A string that represents the image path.
        """
    folder_path = os.getcwd()
    return folder_path + "\images\\fragments"


def verify_if_path_exists(path):
    """
    Verify if the image/folder exists.

    :param path:
    :return: True if the path exists.
    """
    return os.path.exists(path)

def expand_image_first_solution(image,iterations):
    RIGHT_COLUMN_BOUND = get_image_width(fragment_image) - 1
    BOTTOM_ROW_BOUND = get_image_height(fragment_image) - 1

    IMAGE_CENTER_X = int(get_image_width(fragment_image) / 2)
    IMAGE_CENTER_Y = int(get_image_height(fragment_image) / 2)

    START_ROW_VALUE = 1
    START_COLUMN_VALUE = 1

    # FIRST  CASE: FIRST  QUADRANT 1-1
    # SECOND CASE: SECOND QUADRANT 1-110 RIGHT-COLUMN-BOUND
    # THIRD  CASE: THIRD  QUADRANT 110-1 BOTTOM-ROW-BOUND
    # FOURTH CASE: FOURTH QUADRANT 110-110 RIGHT-COLUMN-BOUND BOTTOM-ROW-BOUND
    for i in range(1,iterations):
        image = expand(image, IMAGE_CENTER_X, IMAGE_CENTER_Y, START_ROW_VALUE, START_COLUMN_VALUE)
        image = expand(image, IMAGE_CENTER_X, IMAGE_CENTER_Y, START_ROW_VALUE, RIGHT_COLUMN_BOUND)
        image = expand(image, IMAGE_CENTER_X, IMAGE_CENTER_Y, BOTTOM_ROW_BOUND, START_COLUMN_VALUE)
        image = expand(image, IMAGE_CENTER_X, IMAGE_CENTER_Y, BOTTOM_ROW_BOUND, RIGHT_COLUMN_BOUND, )

    return image


def expand(image,image_center_x,image_center_y,start_row_value,start_column_value):

    # SUGGESTED VALUES ARE 25 AND 80
    MINIMUM_PERCENTAGE_OF_BLACK = 25
    MAXIMUM_PERCETANGE_OF_BLACK = 80

    for row in range(start_row_value, image_center_x):
        for column in range(start_column_value, image_center_y):
            if (is_image_pixel_black(image, row, column)):
                black_neigh_percent = get_percentage_of_black_neighbors(image, row, column)
                if (black_neigh_percent > MINIMUM_PERCENTAGE_OF_BLACK) and (
                        black_neigh_percent < MAXIMUM_PERCETANGE_OF_BLACK):
                    neighbors_color_values = get_neighbors_pixels_colors(image, row, column)
                    for neighbor_value in neighbors_color_values:
                        if (is_pixel_black(neighbor_value)):
                            # It's a bad idea to overwrite a black pixel with another black pixel.
                            pass
                        else:
                            # Choose the last of the neighbours
                            image = change_pixel_color_and_return_image_BGR(image, row, column,
                                                                            get_blue_value_of_a_pixel(neighbor_value),
                                                                            get_green_value_of_a_pixel(neighbor_value),
                                                                            get_red_value_of_a_pixel(neighbor_value))
                            
    return image



def save_image(image, filename="output_img.png"):
    """
    Save the specified image in the "fragments" folder.

    :param image: Image to save
    :param filename: A name for the image with the extension. If not specified the default is output_img.png
    :return:
    """
    folder_path = get_folder_path()
    os.chdir(folder_path)

    try:
        cv2.imwrite(filename, image)
        print("Image saved successfully!")
    except:
        print("Error while saving image!")


if __name__ == "__main__":

    fragment_image = cv2.imread(get_img_path(IMAGE_NAME), cv2.IMREAD_COLOR)


    fragment_image = expand_image_first_solution(fragment_image,20)
    save_image(fragment_image, "OUT_" + IMAGE_NAME)

    cv2.imshow('image', fragment_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
