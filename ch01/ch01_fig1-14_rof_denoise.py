# -*- coding: utf-8 -*-
from PIL import Image
from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
from PCV.tools import rof

""" This is the de-noising example using ROF in Section 1.5. """

im = array(Image.open('../data/empire.jpg').convert('L'))

U,T = rof.denoise(im,im)
G = filters.gaussian_filter(im,10)

# plot
figure()
gray()

subplot(1,3,1)
imshow(im)
axis('off')
title('Original Image')

subplot(1,3,2)
imshow(G)
axis('off')
title('Guassian smoothing')

subplot(1,3,3)
imshow(U)
axis('off')
title('ROF result')

show()