# A list of tesseract utils
import numpy as np
from PIL import Image
import pytesseract

def numpyImageToText(numpyImage):
    img = Image.fromarray(numpyImage)
    return pytesseract.image_to_string(img)
