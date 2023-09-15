import cv2

resim = cv2.imread("Loki Portraet.jpeg", 0)

print(type(resim))

print(resim.size)

print(resim.shape)

print(resim.item(400, 200), 0) #Blue
print(resim.item(400, 200), 1) #Green
print(resim.item(400, 200), 2) #Red

cv2.imshow("Loki Portresi", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()



