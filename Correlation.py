import os
import cv2
import numpy as np

files = os.listdir('Data/')
files.sort()
for file in files:
	f 		= open("Data/" + file, "r")
	x 	= f.readlines()
	x 	= [int(card) for card in x]
	
	y 	= range(52)
	print(file + ' : ' + str(abs(np.corrcoef(x,y)[0,1])))