import numpy as np
import glob
from pdf_reader import const as C
import fitz
from PIL import Image

def pdf_to_images(file):
    docs = fitz.open(stream=file, filetype="pdf")
    images = []

    for page in docs:
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)

    return images

