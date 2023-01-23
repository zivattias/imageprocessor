# def rgb2gs(img: image):
#     # array = np.array(img)
#     # new_array = np.zeros((len(img[0]), len(img)), dtype=np.uint8)
#     # for i, h in enumerate(array):
#     #     for j, w in enumerate(h):
#     #         red = array[i][j][R] * 0.299
#     #         green = array[i][j][G] * 0.587
#     #         blue = array[i][j][B] * 0.114
#     #         gray = red + green + blue
#     #         new_array[i] = int(gray)
#     # gs_img = np.asarray(new_array)
#     # image.imsave('/Users/ziv.attias/PycharmProjects/imageprocessor/samples/koala_edited.jpeg', gs_img)
#     gs = np.dot(img[..., :3], [0.299, 0.587, 0.144])
#     # image.imsave('/Users/ziv.attias/PycharmProjects/imageprocessor/samples/koala_gs.jpeg', gs)
#     return gs