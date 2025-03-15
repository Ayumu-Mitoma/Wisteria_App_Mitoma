import numpy as np
from pdf_reader import const as C
import fitz
from PIL import Image
import io
import base64

def pdf_to_images(file):
    doc = fitz.open(stream = file, filetype="pdf")
    images = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        img_io = io.BytesIO()
        img.save(img_io, format="PNG")
        img_io.seek(0)

        images.append(img_io)

    return images

def get_image_base64(img_io):
    return base64.b64encode(img_io.getvalue()).decode()