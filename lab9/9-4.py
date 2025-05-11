from PIL import Image
watermark = Image.open("C:/Users/Vlad/PycharmProjects/PythonProject2/lab9/watermark.png")
img_watermark = Image.open("C:/Users/Vlad/PycharmProjects/PythonProject2/lab9/cat.jpg")
img_watermark.paste(watermark,(900,550),watermark)
img_watermark.save("C:/Users/Vlad/PycharmProjects/PythonProject2/lab9/cat_withmark.png")