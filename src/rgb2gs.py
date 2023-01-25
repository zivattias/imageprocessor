import os.path

import numpy as np
from matplotlib import pyplot

from load_image import *


def rgb2gs(src: str):
    if not os.path.exists(src):
        raise FileNotFoundError()
    img = load_image(src)
    gs = np.dot(img[..., :3], [0.299, 0.587, 0.144])
    file, ext = os.path.splitext(src)
    pyplot.imsave(f"{file}_gray" + ext, gs, cmap=pyplot.get_cmap('gray'))
    return True


flag = rgb2gs('/Users/ziv.attias/PycharmProjects/imageprocessor/samples/dog.png')
print('Done') if flag else 'Error'
