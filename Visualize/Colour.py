import os
import cv2
import numpy as np

files = os.listdir('../Plots/')

for file in files:
	im = cv2.imread('../Plots/' + file, 0)
	imC = cv2.applyColorMap(im, cv2.COLORMAP_SUMMER)
	cv2.imwrite('../Coloured/' + file, imC)