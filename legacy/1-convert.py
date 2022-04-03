from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

image = Image.open('IMG_0737.HEIC')
image.save("test.jpg", "JPEG")


'''
https://github.com/carsales/pyheif
https://stackoverflow.com/questions/54395735/how-to-work-with-heic-image-file-types-in-python
'''