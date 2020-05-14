import os
import logging
import cv2

from image_manipulator import *


logging.basicConfig(level=logging.DEBUG)

IMAGE_NAME = "frag_107.png"



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



if __name__ == "__main__":
    fragment_image = cv2.imread(get_img_path(IMAGE_NAME), cv2.IMREAD_COLOR)

    print(get_image_size(fragment_image))
    cv2.imshow('image', fragment_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



