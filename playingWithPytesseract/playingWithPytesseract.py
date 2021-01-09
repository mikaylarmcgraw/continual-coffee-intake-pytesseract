import pytesseract as tess
from PIL import Image

img = Image.open('help.png') #paint txt image
img2= Image.open('arialFont.png') #testing arial font
img3= Image.open('ocrImage.png') #invoice

text = tess.image_to_string(img)
text2 = tess.image_to_string(img2)
text3 = tess.image_to_string(img3)

#writing invoice image to file and printing results on console
text_file = open("Output.txt", "w")
text_file.write(text3)
text_file.close()
text_file = open("Output.txt", "r")
print(text_file.read())