import os
from PIL import Image

os.mkdir("pictures")

for i in range(1, 6):
    filename = "lab9/"+str(i)+".jpg"
    image = Image.open(filename)
    image_new = image.convert("L")
    newfilename = "lab9/pictures/"+str(i)+".jpg"
    image_new.save(newfilename)