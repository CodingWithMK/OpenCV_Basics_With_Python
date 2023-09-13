import cv2
import numpy as np

resim = cv2.imread("Seinfeld.jpeg")

cv2.imwrite("Seinfeld_gri.jpg", resim)

cv2.imshow("Seinfeld Resmi", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()



