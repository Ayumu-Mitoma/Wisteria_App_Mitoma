import numpy as np
import glob
from pdf_reader import const as C
import fitz

def pdf_to_images(file):
    docs = fitz.open(stream=file, filetype="pdf")
    images = [page.get_pixmap() for page in docs]
    return [img.pil_save() for img in images]

