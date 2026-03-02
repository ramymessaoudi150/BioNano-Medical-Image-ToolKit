import cv2
import matplotlib.pyplot as plt

image = cv2.imread("brain_mri.jpg", 0)
_, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

plt.imshow(thresh, cmap='gray')
plt.title("Segmented Image")
plt.show()
