import cv2
from PIL import Image;

# im = Image.new(mode="L", size=(200, 200))
# im.show()

img = cv2.imread('test1.jpg', 0)
print(img)

cv2.imwrite('test1_res.jpg', img)
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

