import os
import matplotlib.pyplot as plt
import pandas as pd


def read_images_info():

    root_folder = r'C:\Users\mattw\Documents\Python\BreastCancerDetection\3748_5967_bundle_archive'
    file_name = "info.txt"

    file_path = os.path.join(root_folder, file_name)
    image_info_dict = pd.read_csv(file_path, sep=' ', index_col=0)

    return image_info_dict

def read_images():

    first_img_num = 1
    last_img_num = 322

    images = []

    for curr_img_num in range(first_img_num, last_img_num + 1):
        padded_num = str(curr_img_num).zfill(3)
        file_name = "mdb" + padded_num
        images.append(read_pgm(file_name))

    return images



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

        image_matrix = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(ord(f.read(1)))
            image_matrix.append(row)

    return image_matrix

info = read_images_info()

images = read_images()

plt.matshow(images[100])

plt.show()