
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('ruike.png')  # 读取图像
plt.imshow(img)
plt.show()