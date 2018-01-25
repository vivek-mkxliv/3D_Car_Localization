from glob import glob
import numpy as np
import os, shutil
from PIL import Image


def transfer(src, dst):
    shutil.copyfile(src, dst)

deploy_folder = "C:\\Users\\vivek\\Desktop\\V\\UMich\\S3 - Fall 2017\\ROB 599\\Project\\Perception_v2\\deploy\\"
target_folder = deploy_folder

test_folder = glob(deploy_folder + "test\\*")
testimages_folder = deploy_folder + "testimages\\"

if (os.path.isdir(testimages_folder) == False):
    os.makedirs(testimages_folder)

fils = glob(deploy_folder + "test\\*\\*_image.jpg")
print("\nRestructuring test images to ./testimages/  .....")
for each in test_folder:
	n = str(each) + '\\*_image.jpg'
	files = glob(n)
	# print(files)
	for every in files:
		# print(str(every) + '\n')
		b = str(every).split('\\')
		# print(trrget_folder)
		new_path = testimages_folder + b[12] + '__' + b[13]
		transfer(every, new_path)

print("Creating test.txt  .....")
new_fils = glob(deploy_folder + "testimages\\*_image.jpg")
fil = open(target_folder + "test.txt", 'w')
for each in fils:
	fil.write(each + '\n')
fil.close()