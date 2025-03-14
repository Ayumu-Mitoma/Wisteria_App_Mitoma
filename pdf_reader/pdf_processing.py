import numpy as np
import glob
from pdf_reader import const as C
from pdf2image import convert_from_bytes

def pdf_to_images(file):
    images = convert_from_bytes(file, dpi=600)
    return images

