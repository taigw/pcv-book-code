# -*- coding: utf-8 -*-
from PIL import Image
from numpy import *
from scipy.ndimage import measurements, morphology
from pylab import *

"""   This is the morphology counting objects example in Section 1.4.  """

# load image and threshold to make sure it is binary
figure()
gray()
im = array(Image.open('../data/houses.png').convert('L'))
subplot(221)
imshow(im)
axis('off')
im = (im < 128)

labels, nbr_objects = measurements.label(im)
print("Number of objects:", nbr_objects)
subplot(222)
imshow(labels)
axis('off')

# morphology - opening to separate objects better
im_open = morphology.binary_opening(im, ones((9, 5)), iterations=2)
subplot(223)
imshow(im_open)
axis('off')

labels_open, nbr_objects_open = measurements.label(im_open)
print("Number of objects:", nbr_objects_open)
subplot(224)
imshow(labels_open)
axis('off')

show()