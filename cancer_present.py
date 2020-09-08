import torch
import torch.nn as nn
import torch.nn.functional as F
from visualisation import read_pgm, read_images_info

input = []
for image_num in range(1, 323):
    image_name = "mdb" + str(image_num).zfill(3)
    image_matrix = read_pgm(image_name)
    input.append([item for sublist in image_matrix for item in sublist])

print(len(input), len(input[0]))

