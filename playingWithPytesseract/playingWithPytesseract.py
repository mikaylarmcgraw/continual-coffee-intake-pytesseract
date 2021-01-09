import pytesseract as tess
from PIL import Image

img = Image.open('help.png')
img2= Image.open('arialFont.png')
text = tess.image_to_string(img)
text2 = tess.image_to_string(img2)

text_file = open("Output.txt", "w")
text_file.write(text + text2)
text_file.close()