import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('view.jpg', cv2.IMREAD_COLOR)

print(f"图像的数据类型: {type(image)}")
print(f"图像的维度 (高, 宽, 通道数): {image.shape}")
print(f"图像的数据类型: {image.dtype}")

