def change_pixel_color_and_return_image_RGB(opened_image, x, y, red_value, green_value, blue_value):
    opened_image[x, y] = [red_value, green_value, blue_value]
    return opened_image


def get_neighbors_pixels_colors(opened_image, x, y):
    pixels_colors_values_list = []
    for row in range(x - 1, x + 2):
        for column in range(y - 1, y + 2):
            if(row == 1) and (column == 1):
                pass
            else:
                pixels_colors_values_list.append(opened_image[row,column])

    return pixels_colors_values_list


def get_pixel_color(opened_image,x,y):
    return opened_image[x,y]
