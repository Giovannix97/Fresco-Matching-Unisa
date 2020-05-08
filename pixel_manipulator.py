def change_pixel_color_and_return_image_RGB(opened_image, pixel_x, pixel_y, red_value, green_value, blue_value):
    opened_image[pixel_x, pixel_y] = [red_value, green_value, blue_value]
    return opened_image


def get_neighbors_pixels_colors(opened_image, pixel_x, pixel_y):
    pixels_colors_values_list = []
    for row in range(pixel_x-1, pixel_x+2):
        for column in range(pixel_y-1, pixel_y+2):
            if(row == 1) and (column == 1):
                pass
            else:
                pixels_colors_values_list.append(opened_image[row,column])

    return pixels_colors_values_list
