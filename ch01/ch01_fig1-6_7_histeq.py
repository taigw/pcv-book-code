 # -*- coding: utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
from pylab import *
from PCV.tools import imtools

# im = array(Image.open('../data/empire.jpg').convert('L'))  # 打开图像，并转成灰度图像
im = array(Image.open('../data/AquaTermi_lowcontrast.JPG').convert('L'))
im2, cdf = imtools.histeq(im)

figure()
subplot(2, 3, 1)
xticks([]); yticks([])
hist(im.flatten(), 128)

subplot(2, 3, 2)
xticks([]); yticks([])
plot(range(256),list(cdf))

subplot(2, 3, 3)
xticks([]); yticks([])
hist(im2.flatten(), 128)

subplot(2, 3, 4)
axis('off')
gray()
imshow(im)

subplot(2, 3, 6)
axis('off')
gray()
imshow(im2)

show()
