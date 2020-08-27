import os
import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np


def read_images_info():

    root_folder = r'C:\Users\mattw\Documents\Python\BreastCancerDetection\3748_5967_bundle_archive'
    file_name = "info.txt"

    file_path = os.path.join(root_folder, file_name)
    img_info_df = pd.read_csv(file_path, sep=' ', index_col=0)

    return img_info_df


def read_pgm(file_name):
    """

    https://stackoverflow.com/questions/35723865/read-a-pgm-file-in-python
    :param file_name:
    :return:
    """

    root_folder = r'C:\Users\mattw\Documents\Python\BreastCancerDetection\3748_5967_bundle_archive\all-mias'
    file_name_w_ext = file_name + ".pgm"
    file_path = os.path.join(root_folder, file_name_w_ext)

    with open(file_path, 'rb') as f:
        assert f.readline() == b'P5\n'
        width, height = (int(val) for val in f.readline().split())
        depth = int(f.readline())
        assert depth <= 255

        img_matrix = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(ord(f.read(1)))
            img_matrix.append(row)

    return img_matrix

def show_scan(image_num):

    assert isinstance(image_num, int) and image_num >= 1 and image_num <= 322

    image_name = "mdb" + str(image_num).zfill(3)

    image_info_df = read_images_info()
    curr_img_info_srs = image_info_df.loc[image_name, :]
    print(curr_img_info_srs.RADIUS)

    img_matrix = read_pgm(image_name)

    plt.matshow(img_matrix, cmap="Blues")

    if not math.isnan(curr_img_info_srs.RADIUS):
        plt.scatter(curr_img_info_srs.X, curr_img_info_srs.Y, c='r')

        x = []
        y = []
        for theta in np.linspace(0, 2 * math.pi, 100):
            x.append(curr_img_info_srs.X + curr_img_info_srs.RADIUS * math.cos(theta))
            y.append(curr_img_info_srs.Y + curr_img_info_srs.RADIUS * math.sin(theta))

        plt.plot(x, y, c='r')

        plt.title(f"{image_name} ({int(curr_img_info_srs.X)}, {int(curr_img_info_srs.Y)}) R: {int(curr_img_info_srs.RADIUS)}")

    else:
        plt.title(image_name)


    plt.show()




show_scan(5)