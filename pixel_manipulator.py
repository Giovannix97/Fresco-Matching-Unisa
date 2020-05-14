def get_pixel_color(image, x, y):
    """
    Return BGR specified pixel color value

    :param image:
    :param x:
    :param y:
    :return: A BGR value associated to the pixel.
    """
    if(x < 0) or (y < 0):
        raise Exception("X or Y value cannot be negative!")
    return image[x, y]


def change_pixel_color_and_return_image_RGB(image, x, y, blue_value, green_value, red_value):
    """
    Manipulate BGR value of a specified pixel and returns a new image

    N.B. OpenCv uses BGR instead of RGB.

    :param image:
    :param x:
    :param y:
    :param blue_value: int value from 0 to 255
    :param green_value: int value from 0 to 255
    :param red_value: int value from 0 to 255
    :return: A new manipulated image.


    """
    image[x, y] = [blue_value, green_value, red_value]
    return image


def get_neighbors_pixels_colors(image, x, y):
    """
    Return a list that contains all the neighbors of the specified pixel.

    Let's consider a 3x3 matrix, in which the considered pixel is located at the center.
    Starting from the top left corner and sliding each single row, all the BGR are stored
    in the returned list.

    :param image:
    :param x:
    :param y:
    :return: A list of 8 BGR values
    """
    pixels_colors_values_list = []
    for row in range(x - 1, x + 2):
        for column in range(y - 1, y + 2):
            if(row == x) and (column == y):
                pass
            else:
                pixels_colors_values_list.append(image[row, column])

    return pixels_colors_values_list


