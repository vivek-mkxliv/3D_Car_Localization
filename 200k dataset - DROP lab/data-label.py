import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

path = 'D:\\Driving in the Matrix'
target_path = 'D:\\Driving in the Matrix'

k = 'VOC2012'
size = '200k'

image_set = 'train200k'

classes = ["car"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(k, image_id):
    in_file = open('%s/VOC2012/Annotations/%s.xml'%(path, image_id))
    out_file = open('%s/VOC2012/labels/%s.txt'%(path, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

# wd = getcwd()
# wd = 'D:/599 - Darknet - Windows/build/darknet/x64/data/voc/'
# wd = 'data'

# for k, image_set in sets:
if not os.path.exists('%s/VOC2012/labels/'%(path)):
    os.makedirs('%s/VOC2012/labels/'%(path))
image_ids = open('%s/VOC2012/ImageSets/Main/trainval%s.txt'%(path, size)).read().strip().split()
list_file = open('%s/%s.txt'%(target_path, image_set), 'w')
for image_id in image_ids:
    list_file.write('%s/VOC2012/JPEGImages/%s.jpg\n'%(target_path, image_id))
    # list_file.write('%s/JPEGImages/%s.jpg\n'%(wd, k, image_id))
    convert_annotation(k, image_id)
list_file.close()

