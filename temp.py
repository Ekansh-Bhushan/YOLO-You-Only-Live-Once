import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

img =Image.open(r"C:/Users/Ekansh/code/vihaan007/sample2.jpg")
text=list(tess.image_to_string(img).splitlines())

print(text)


print(text)