
# Importing Image and ImageFilter module from PIL package  
from PIL import Image, ImageFilter 
     
# creating a image object 
im1 = Image.open(r"filter-test.png") 
     
# applying the median filter 
#size adjusts the kernal size (more median filter)
im2 = im1.filter(ImageFilter.MedianFilter(size = 3)) 
     
im2.show() 

'''
https://www.geeksforgeeks.org/python-pil-medianfilter-and-modefilter-method/
'''