#######################################
# import libraries and useful modules #
#######################################
from PIL import Image, ImageFilter, ImageStat
from pillow_heif import register_heif_opener


####################################
# convert from HEIC to PNG to JPEG #
####################################
register_heif_opener()

im_heic = Image.open(r"images/image.HEIC")
im_heic.save(r"images/image.png", "PNG")

im_png = Image.open(r"images/image.png")
img_jpg = im_png.save(r"images/image.jpg", "JPEG")


################
# filter image #
################
im = Image.open(r"images/image.jpg")
     
# apply median filter 
# note: increasing size adjusts the kernal size and increases filter intensity
im_filtered = im.filter(ImageFilter.MedianFilter(size = 7)).save(r"images/image_filtered.jpg")


##############
# crop image #
##############
im_2 = Image.open(r"images/image_filtered.jpg")

# note: im.crop(x-left, y-top, x-right, y-bottom)
# crop left region and rgb color swatches
region_left = im.crop((850, 320, 1210, 1000)).save(r"images/region_left.jpg")
r_swatch_left = im.crop((800, 110, 900, 210)).save(r"images/r_swatch_left.jpg")
g_swatch_left = im.crop((965, 120, 1060, 210)).save(r"images/g_swatch_left.jpg")
b_swatch_left = im.crop((1120, 125, 1220, 210)).save(r"images/b_swatch_left.jpg")

# crop right region and rgb color swatches
region_right = im.crop((1340, 320, 1740, 970)).save(r"images/region_right.jpg")
r_swatch_right = im.crop((1325, 130, 1415, 220)).save(r"images/r_swatch_right.jpg")
g_swatch_right = im.crop((1480, 130, 1570, 220)).save(r"images/g_swatch_right.jpg")
b_swatch_right = im.crop((1640, 140, 1730, 220)).save(r"images/b_swatch_right.jpg")


#################
# rgb averaging #
#################
def average(image_path):
    im_3 = Image.open(image_path)
    stat = ImageStat.Stat(im_3)
    rgb = stat.mean
    
    r, g, b = rgb
    r = round(r)
    g = round(g)
    b = round(b)
    rgb_average = [r, g, b]
    #print(rgb_average)
    return rgb_average

#print("region_left_avg: ")
region_left_avg = average(r"images/region_left.jpg")
#print("r_swatch_left_avg: ")
r_swatch_left_avg = average(r"images/r_swatch_left.jpg")
#print("g_swatch_left_avg: ")
g_swatch_left_avg = average(r"images/g_swatch_left.jpg")
#print("b_swatch_left_avg: ")
b_swatch_left_avg = average(r"images/b_swatch_left.jpg")

#print("region_right_avg: ")
region_right_avg = average(r"images/region_right.jpg")
#print("r_swatch_right_avg: ")
r_swatch_right_avg = average(r"images/r_swatch_right.jpg")
#print("g_swatch_right_avg: ")
g_swatch_right_avg = average(r"images/g_swatch_right.jpg")
#print("b_swatch_right_avg: ")
b_swatch_right_avg = average(r"images/b_swatch_right.jpg")

#print("region left average: ", region_left_avg)
#print("region left average: ", region_right_avg)


####################
# color correction #
####################
# pure rgb values within the color gamut of a cmyk printer
r_pure = [237, 32, 36]
g_pure = [106, 189, 69]
b_pure = [57, 83, 164]

# calculate rgb weights (% difference from pure) of left test
r_weight_left = 1 + ((r_pure[0] - r_swatch_left_avg[0]) / r_pure[0])
g_weight_left = 1 + ((g_pure[1] - g_swatch_left_avg[1]) / g_pure[1])
b_weight_left = 1 + ((b_pure[2] - b_swatch_left_avg[2]) / b_pure[2])

# calculate rgb weights of right test
r_weight_right = 1 + ((r_pure[0] - r_swatch_right_avg[0]) / r_pure[0])
g_weight_right = 1 + ((g_pure[1] - g_swatch_right_avg[1]) / g_pure[1])
b_weight_right = 1 + ((b_pure[2] - b_swatch_right_avg[2]) / b_pure[2])

# print(r_weight_left, g_weight_left, b_weight_left)
# print(r_weight_right, g_weight_right, b_weight_right)


#####################################
# calculate biomarker concentration #
#####################################
# CysC calibration curve data
r_int_CysC = 313.4999999999999
r_slope_CysC = -167.49999999999991
g_int_CycC = 376.8571428571427
g_slope_CysC = -193.57142857142847
b_int_CysC = 346.07142857142856
b_slope_CysC = -133.21428571428572

# Alb calibration curve data
r_int_Alb = 286.4285714285713
r_slope_Alb = -5.028571428571422
g_int_Alb = 229.7142857142855
g_slope_Alb = -1.214285714285704
b_int_Alb = 174.9999999999999
b_slope_Alb = -1.8999999999999952

# calculate the concentration of left uPAD (CysC) and apply color correction
r_concentration_left = ((r_weight_left * region_left_avg[0]) - r_int_CysC) / r_slope_CysC
g_concentration_left = ((g_weight_left * region_left_avg[1]) - g_int_CycC) / g_slope_CysC
b_concentration_left = ((b_weight_left * region_left_avg[2]) - b_int_CysC) / b_slope_CysC

# calculate the concentration of right uPAD (Alb) and apply color correction
r_concentration_right = ((r_weight_right * region_right_avg[0]) - r_int_Alb) / r_slope_Alb
g_concentration_right = ((g_weight_right * region_right_avg[1]) - g_int_Alb) / g_slope_Alb
b_concentration_right = ((b_weight_right * region_right_avg[2]) - b_int_Alb) / b_slope_Alb

# calculate average conentration of all color bands
rgb_concentration_left = (r_concentration_left + g_concentration_left + b_concentration_left) / 3
rgb_concentration_right = (r_concentration_right + g_concentration_right + b_concentration_right) / 3

# display [biomarker] values
print("\n")
print("The concentraiton of cystatin C in mg/dL = ")
print(rgb_concentration_left)
print("The concentraiton of albumin in mg/g = ")
print(rgb_concentration_right)