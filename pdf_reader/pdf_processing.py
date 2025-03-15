import numpy as np
import glob
from pdf_reader import const as C
import fitz

def pdf_to_images(file):
    docs = fitz.oepn(stream=file, filetype="pdf")
    images = [page.get_pixamp() for page in docs]
    return images

