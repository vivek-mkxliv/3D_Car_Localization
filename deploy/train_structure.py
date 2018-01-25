from glob import glob
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import os, shutil
from PIL import Image

def transfer(src, dst):
    shutil.copyfile(src, dst)


# files = glob('\\home\\divyansh\\PycharmProjects\\darknet\\rob599_dataset_deploy\\trainval\\*\\*_image.jpg')
deploy_folder = "C:\\Users\\vivek\\Desktop\\V\\UMich\\S3 - Fall 2017\\ROB 599\\Project\\Perception_v2\\deploy\\"
target_folder = deploy_folder + "obj\\"
traintxt_folder = deploy_folder

if (os.path.isdir(target_folder) == False):
    os.makedirs(target_folder)

files = glob(deploy_folder + "trainval\\*\\*_image.jpg")

i = 0
print("\nRestructuring training images and corresponding labels to ./obj/  .....")
for each in files:
    # print(each)
    new_path = target_folder + str(i) + ".jpg"
    # print(new_path)
    transfer(each, new_path)

    label = each.replace(".jpg",".txt")
    # print(label)
    new_path_label = target_folder + str(i) + ".txt"
    # print(new_path)
    transfer(label, new_path_label)
    i = i+1

print("Creating train.txt  .....")
fils = glob(target_folder + "*.jpg")
fil = open(traintxt_folder + "train6k.txt", 'w')
for each in fils:
    fil.write(each + '\n')
fil.close()



# print(len(files))
"""for i in range(len(files)):
# for i in range(4):
# idx = np.random.randint(0, len(files))
    snapshot = files[i]
    # print(snapshot)
    img = plt.imread(snapshot)
    try:
        bbox = np.fromfile(snapshot.replace('_image.jpg', '_bbox.bin'), dtype=np.float32)
    except:
        print('[*] bbox not found.')

    # try:
    #     label = np.fromfile(snapshot.replace('_image.jpg', '_image.txt'), dtype=np.float32)
    #     print(label)
    # except:
    #     print('[*] Label Text file not found.')
    label_path = snapshot.replace('_image.jpg', '_image.txt')

    bbox.resize([bbox.size // 11, 11])
    for every in bbox:
        class_num = every[9]
        print(class_num)
        path = "\\home\\divyansh\\PycharmProjects\\darknet\\rob599_dataset_deploy\\obj\\" + str(class_num)


        # print(path)
        if (os.path.isdir(path) == False):
            os.makedirs(path)
        imgn = Image.fromarray(img)
        new_path = path+"\\" + str(i) + ".jpg"
        print(new_path)
        imgn.save(new_path)


        ## Uncomment this portion when text files are added
        # if label != 0:

        path_lab = "\\home\\divyansh\\PycharmProjects\\darknet\\rob599_dataset_deploy\\obj\\" + str(class_num)
        if (os.path.isdir(path_lab) == False):
            os.makedirs(path_lab)

        # print(label)
        transfer(label_path, path_lab + '\\' + str(i) + '.txt')"""