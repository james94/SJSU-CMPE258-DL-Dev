"""
pdisplay.py
Demo read and display image

Based on Dr Li's Py Script: https://github.com/hualili/opencv/blob/master/deep-learning-2022s/2022S-104d-%232-pdisplay-2019-1-30.py
"""
import sys
import cv2
import numpy as np

#main(sys.argv[1:])
window_name = 'Display Image'
 
imageName = sys.argv[1] #get file name from command line 

src = cv2.imread(imageName, cv2.IMREAD_COLOR)

if src is None:
   print ('Error opening image!')
   print ('Usage: pdisplay.py image_name\n')
  
ind = 0

while True: 
    cv2.imshow(window_name, src)

    c = cv2.waitKey(500)
    if c == 27:  #ESC
       break

    ind += 1