from PIL import Image

file_path = r'../Pictures/1.jpg'

img = Image.open(file_path)

print(f'Размер изображения: {img.width}x{img.height}')
print(f'Формат: {img.format}')
print(f'Цветовая модель: {img.mode}')

img.show()