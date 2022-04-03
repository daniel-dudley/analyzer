#import modules
#import cv2
from PIL import Image, ImageStat

#open image and find RGB average
im = Image.open('average-test.jpg')
stat = ImageStat.Stat(im)
rgb = stat.mean
print(rgb)

#break list into varibles
r, g, b = rgb
r = round(r)
g = round(g)
b = round(b)

print(r)
print(g)
print(b)

rgb_color = [r, g, b]
def rgb_to_hex(rgb_color):
    hex_color = "" #there was a '#' here
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color

x_hex = (rgb_to_hex(rgb_color))
print(x_hex)

dec = int(x_hex, 16)


print('Value in hexadecimal:', x_hex)
print('Value in decimal:', dec)


'''
https://www.tutorialspoint.com/calculating-the-mean-of-all-pixels-for-each-band-in-an-image-using-the-pillow-library
'''

'''
def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(r, g, b)

print(rgb_to_hex(r, g, b))
'''

'''
# hexadecimal string
hex = 'ffffc7' 
 
# conversion
dec = int(hex, 16)
'''

''' 
print('Value in hexadecimal:', hex)
print('Value in decimal:', dec)
'''

'''
Need to convert RGB to hex to create standard curve...
Convert Hex to decimal for use in standard curve...
    https://www.pythonpool.com/python-hexadecimal-to-decimal/#:~:text=Python%20module%20provides%20an%20int,an%20integer%20of%20base%2010.
'''