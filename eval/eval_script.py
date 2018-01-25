# Input is the output of 3dbbox.py given as 3D bounding box coordinates and dimensions, with a threshold of 0.01%

########################################
########################################
#            LIBRARIES
########################################
########################################
from glob import glob
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math
import os, shutil
from PIL import Image


########################################
########################################
#           SET THRESHOLD
########################################
########################################
# Set threshold of the detection here
threshold = 40.0
# threshold = 35.0      # .... Sweet Spot !!
# threshold = 30.0


########################################
########################################
#             FUNCTIONS
########################################
########################################
# root(x^2 + y^2 + z^2) less than equal to 60 m
# distance check (values in meters) (convert the output of valid file 2D bounding boxes to 3D bounding box in meters using the 3dbbox.py)
def distance_check(x, y, z):
    dist = math.sqrt((x*x) + (y*y) + (z&*z))
    if (disy <= 60.0):
        return 1
    else:
        return 0

# Mostly visible. z should be greater than equal to root(max(0, a^2x^2 - l^2)) a = tan(50 degree) l = 3
def visibility_check(x, z, l):
    a = math.tan(50*np.pi/180)
    visib = math.sqrt(max(0, ((a*a*x*x)-(l*l))))
    if (z >= visib):
        return 1
    else:
        return 0

#Occlusion should be less than equal to 40% 2D
def overlap_check():
    # check area of the bounding box and compare it with all the valid bounding boxes
    # THe 2D area of the bounding box should not overlap another bounding box by more than 40%

    # Check the ratio of width and height, for both cases :
    # 1. when the car is facing towards/away from the camera (aligned with the camera angle, either positively or negatively (respectively))
    # 2. when the orientation of the car is not aligned to the camera (either positive or negative alignment)
    pass


# Check if class needs to be counted or not
def class_check(clas):
    class_list = [1,2,3,4,5,6,7,8,10,12,13,18,19,20]
    if clas in class_list:
        return 1
    else:
        return 0

def prob_check(clas_probability):
    if clas_probability >= threshold:
        return 1
    else:
        return 0

# Volume of bounding box should be less than equal to 50 m^3
def volume_check(l, w, h):
    vol = l*w*h
    if (vol <= 50):
        return 1
    else:
        return 0

# If two boxes nearly overlap, take the higher confidence value box
def duplicacy_check():
    pass

# If area of bounding box is less than a threshold value discard it
def area_check():
    pass


def min_max(count):
    if count > 12:
        return 12
    elif count < 1:
        return 0
    else:
        return count


########################################
########################################
#                MAIN
########################################
########################################
def main():
    path = "D:\\Team 2 - Knights\\eval\\"
    final_result = path + "final_result_3d.txt"
    input_file = path + "r599-detection-3d-bbox.txt"
    #input_file = 'D:\\599 - Perception\\r599-detection-3d-bbox.txt'

    main_file = open(final_result, 'w')
    main_file.write('guid/image,N\n')
    fil = open(input_file, 'r')
    a = fil.readlines()
    guid_image = ''
    old = guid_image
    count = 0
    for each in a:
        if (each != '\n'):
            # print(each)
            str(each).rstrip('\n')
            b = str(each).split(',')
            # print(b)

            path = b[0]
            cl = int(str(b[1]).strip())
            x = float(str(b[2]).strip())
            y = float(str(b[3]).strip())
            z = float(str(b[4]).strip())
            l = float(str(b[5]).strip())
            w = float(str(b[6]).strip())
            h = float(str(b[7]).strip())
            prob = float(str(b[8]).strip())

            path = path.split('\\')[-1]
            guid = path.split('__')[0]

            image = path.split('__')[-1]
            image = image.split('_')[0]
            guid_image = guid + '/' + image

            if guid_image != old:
                if old != '':
                    count = min_max(count)
                    main_file.write(old + ',' + str(count) + '\n')
                    if prob_check(prob) == 1 and distance_check(x, y, z) == 1 and volume_check(l, w, h) == 1:# and visibility_check(x, z, l) == 1:
                        count = class_check(cl)
                    else:
                        count = 0
                old = guid_image
            else:
                if prob_check(prob) == 1 and distance_check(x, y, z) == 1 and volume_check(l, w, h) == 1:# and visibility_check(x, z, l) == 1:
                    ch = class_check(cl)
                    if ch == 1:
                        count += ch
    main_file.write(old + ',' + str(count))

    main_file.close()



if __name__ == "__main__":
    main()