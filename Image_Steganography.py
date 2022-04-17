import cv2
import numpy as np
from PIL import Image

#it converts data in binary format


def data2binary(data):
    if type(data) == str:
        p = ''.join([format(ord(i), '08b')for i in data])
    elif type(data) == bytes or type(data) == np.ndarray:
        p = [format(i, '08b')for i in data]
    return p


# hide data in given img

def hidedata(img, data):
    data += "$$"               #'$$'--> secret key
    d_index = 0
    b_data = data2binary(data)
    len_data = len(b_data)

