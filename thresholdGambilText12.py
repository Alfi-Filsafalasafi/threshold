# pip install pytesseract (pengenalan karakter)
import pytesseract as pt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
pt.pytesseract.tesseract_cmd = r'C:\Users\Filsafalasafi\AppData\Local\Tesseract-OCR\Tesseract.exe'

img = mpimg.imread('gambarKetigaa.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread('gambarKetigaa.png',0)
plt.hist(img2.ravel(), 256, [0,256])
plt.show()

