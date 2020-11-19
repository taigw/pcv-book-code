# -*- coding: utf-8 -*-
from PIL import Image
from pylab import *
from scipy.ndimage import filters
import numpy

im = array(Image.open('../data/empire.jpg').convert('L'))
gray()

subplot(1, 4, 1)
axis('off')
title('original image')
imshow(im)

# Sobel derivative filters
imx = zeros(im.shape)
filters.sobel(im, 1, imx)
subplot(1, 4, 2)
axis('off')
title('Gx')
imshow(imx)

imy = zeros(im.shape)
filters.sobel(im, 0, imy)
subplot(1, 4, 3)
axis('off')
title('Gx')
imshow(imy)

mag = 255-numpy.sqrt(imx**2 + imy**2)
subplot(1, 4, 4)
title('magnitude')
axis('off')
imshow(mag)

show()
