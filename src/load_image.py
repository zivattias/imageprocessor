from matplotlib import image, pyplot

__all__ = [
    'load_image',
    'show_image',
    'img_shape',
]


def load_image(src: str):
    """
    Loads an array-based image using MATPLOTLIB
    """
    img = image.imread(src)
    return img


def show_image(img: image):
    """
    Presents image in Python-default image presenter
    """
    pyplot.imshow(img)
    pyplot.show()


def img_shape(img: image):
    """
    Returns a 3-item tuple containing width, height and dimensions respectively
    """
    return img.shape
