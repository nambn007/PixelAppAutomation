# import cv2
# import numpy as np
# image = cv2.imread("images/overview.png")
# cv2.rectangle(image, (100, 100), (100 + 15, 100 + 15), (0, 255, 0), 2)
#
# cv2.imwrite("test.jpg", image)
#
# height, width = image.shape[:2]
#
# print("haiz> ",height,width)
#

#
from PIL import Image
import pyscreeze


def get_position(screen_shot_path: str, reg_path: str):
    global x, y
    big = Image.open(screen_shot_path);
    small = Image.open(reg_path);

    locations = pyscreeze.locateAll(small, big)
    for locate in locations:
        x = locate[0]
        y = locate[1]
        print("click at ", x, y)
    return x, y

#
# def calculate_new_coordinates(x, y, scale_factor=0.68):
#     """
#     Calculate new coordinates after applying a scale factor.
#
#     Parameters:
#     - x (int): The original x-coordinate.
#     - y (int): The original y-coordinate.
#     - scale_factor (float): The scale factor to apply, default is 0.68.
#
#     Returns:
#     - tuple: A tuple containing the new x and y coordinates.
#     """
#     new_x = int(x * scale_factor)
#     new_y = int(y * scale_factor)
#     return (new_x, new_y)
