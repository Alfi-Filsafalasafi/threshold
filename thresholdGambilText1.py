# pip install pytesseract (pengenalan karakter)
import pytesseract as pt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
from PIL import Image
pt.pytesseract.tesseract_cmd = r'C:\Users\Filsafalasafi\AppData\Local\Tesseract-OCR\Tesseract.exe'

img = mpimg.imread('gambarKetigaa.png')


img2 = Image.open('gambarKetigaa.png')
text = pt.image_to_string(img2)
print(text)
plt.imshow(img)
plt.show()