# -*- coding: utf-8 -*-
from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
from PCV.tools import rof

""" This is the de-noising example using ROF in Section 1.5. """

# create synthetic image with noise
im = zeros((500,500))
im[100:400,100:400] = 128
im[200:300,200:300] = 255
im = im + 30*random.standard_normal((500,500))

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