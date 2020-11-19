 # -*- coding: utf-8 -*-
from PIL import Image
from pylab import *
from scipy.ndimage import filters

im = array(Image.open('../data/empire.jpg').convert('L'))

figure()
gray()
axis('off')
subplot(1, 4, 1)
axis('off')
title('original image')
imshow(im)

for bi, blur in enumerate([2, 5, 10]):
  im2 = zeros(im.shape)
  im2 = filters.gaussian_filter(im, blur)
  im2 = np.uint8(im2)
  imNum=str(blur)
  subplot(1, 4, 2 + bi)
  axis('off')
  title('sigma='+imNum)
  imshow(im2)

show()
