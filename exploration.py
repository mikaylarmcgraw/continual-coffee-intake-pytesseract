try:
    from PIL import Image
except ImportError:
    import Image

from pytesseract import Output
import cv2

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def DrawBoundaries(fileName):
    img = cv2.imread(fileName)

    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)

def ExtractData(fileName):
    print(fileName + ' contains:')
    print(pytesseract.image_to_data(Image.open(fileName)))

def ExtractString(fileName):
    print(fileName + ' contains:')
    print(pytesseract.image_to_string(Image.open(fileName)))

if(__name__ == "__main__"):
    DrawBoundaries('test.png')
    ExtractData('bettertest.png')
    ExtractString('s-l1600.jpg')
