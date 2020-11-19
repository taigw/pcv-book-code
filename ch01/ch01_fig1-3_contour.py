 # -*- coding: utf-8 -*-
from PIL import Image
from pylab import *

im = array(Image.open('../data/empire.jpg').convert('L')) 
figure()
subplot(121)
gray()
contour(im, origin='image')
axis('equal')
axis('off')

subplot(122)
hist(im.flatten(), 128)
plt.xlim([0,260])
plt.ylim([0,12000])

show()
