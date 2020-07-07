import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Phani\AppData\Local\Tesseract-OCR\tesseract.exe'

imag=Image.open('sample_image.png')
text=pytesseract.image_to_string(imag)

print(text)
