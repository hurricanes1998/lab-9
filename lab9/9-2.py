
from PIL import Image
image = Image.open("cat.jpg")

res_img = image.reduce(2)
res_img.save("red_cat.jpg")

flip_img = image.transpose(Image.FLIP_LEFT_RIGHT)
flip_img.save("flip_cat.jpg")

updown_img = image.transpose(Image.FLIP_TOP_BOTTOM)
updown_img.save("updown_cat.jpg")