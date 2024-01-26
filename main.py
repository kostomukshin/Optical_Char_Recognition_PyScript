import pytesseract
from PIL import Image

#img = Image.open('snap-test.PNG')
#img = Image.open('numbers-test.PNG')
img = Image.open('text-test.PNG')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file_name = img.filename
file_name = file_name.split('.')[0]

#custom_config = r'--oem 3 --psm 12'
#custom_config = r'--oem 3 --psm 4'
custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, config=custom_config)
print(text)

with open(f'{file_name}.txt', 'w') as text_file:
   text_file.write(text)


