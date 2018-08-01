import os
import cv2
import numpy as np

files = os.listdir('../Data/')

for file in files:
	f 		= open("../Data/" + file, "r")
	deck 	= f.readlines()
	deck 	= [int(card) for card in deck]
	
	img 	= np.zeros((1000, 260))

	for i in range(52):
		img[:, 5*i:5*i + 5] = deck[i]*256.0/52

	cv2.imwrite('..Plots/' + file + '.png', img)