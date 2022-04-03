#Import useful stuff
import os, sys
import PIL
from PIL import Image, ImageFilter

'''
#Convert image to JPEG
for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)
'''

#path = "RGB - 3 reservoir paper design test using inkscape.jpg";

#image import
im = Image.open("RGB - 3 reservoir paper design test using inkscape.png")
print("The size of the image before conversion : ", end = "")
print(os.path.getsize("RGB - 3 reservoir paper design test using inkscape.png"))
  
#converting to jpg
rgb_im = im.convert("RGB")
  
#exporting the image
rgb_im.save("TEST3_jpeg.jpg")
print("The size of the image after conversion : ", end = "")
print(os.path.getsize("TEST3_jpeg.jpg"))

'''
im = Image.open("RGB - 3 reservoir paper design test using inkscape.jpg")
im.show("RGB - 3 reservoir paper design test using inkscape.jpg")
print(im.format, im.size, im.mode)
'''

'''
# importing the module
from PIL import Image
import os
  
# importing the image 
im = Image.open("geeksforgeeks.png")
print("The size of the image before conversion : ", end = "")
print(os.path.getsize("geeksforgeeks.png"))
  
# converting to jpg
rgb_im = im.convert("RGB")
  
# exporting the image
rgb_im.save("geeksforgeeks_jpg.jpg")
print("The size of the image after conversion : ", end = "")
print(os.path.getsize("geeksforgeeks_jpg.jpg"))
'''