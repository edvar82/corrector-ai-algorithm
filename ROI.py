import cv2
import numpy as np
 
if __name__ == '__main__' :
 
    # Read image
    im = cv2.imread("recorte.png")
 
    # Select multiple ROIs
    rois = []
    while True:
        r = cv2.selectROI(im)
        if r == (0, 0, 0, 0):  # User pressed 'c' to cancel
            break
        rois.append(r)
 
    # Crop images
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    print(rois)
    cv2.waitKey(0)
