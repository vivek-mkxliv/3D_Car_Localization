# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:11:32 2017

@author: Ignacio Estrada
"""
##############################################################################
##############################################################################
"                       Libraries                                            "
##############################################################################
##############################################################################
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
import glob
##############################################################################
##############################################################################
"                       Functions                                            "
##############################################################################
##############################################################################

def load_pc_from_bin(bin_path):
    """Load PointCloud data from pcd file."""
    obj = np.memmap(bin_path, dtype=np.float32)
    obj.resize([3, obj.size // 3])
    return obj

##############################################################################
##############################################################################
"                       Main Code                                            "
##############################################################################
##############################################################################

" Read in File containing 2D bounding box data "
raw_path = 'D:\\Team 2 - Knights\\3dbbox\\r599-detection-v2.txt';
raw_data = open(raw_path,'r')

bbox_2d = raw_data.readlines()

identifier=[]
classes=[]
bbox_x=[]
bbox_y=[]
bbox_w=[]
bbox_h=[]
bbox_conf=[]
rr_path=[]

" Get x and y pixel coordinates from 2D bbox data"
for line in bbox_2d:
    item=line.split(",")
    rr_path.append(item[0])
    identifier.append(item[0][:-16])
    classes.append(item[1])
    bbox_x.append(item[2])
    bbox_y.append(item[3])
    bbox_w.append(item[4])
    bbox_h.append(item[5])
    bbox_conf.append(item[6])
    
" Read in Camera Projection Matrix & LiDar Points, Project to 2D "
points=[]
camera=[]
uv=[]
counter=0


for item in identifier:
    path=str(item) + str('\\')    
    for infile in glob.glob(os.path.join(path,"*cloud.bin") ):
        points.append((load_pc_from_bin(infile)));
        
    for infile in glob.glob(os.path.join(path,"*proj.bin") ):
        camera.append(load_pc_from_bin(infile));
    
    uv.append(camera[counter] @ np.vstack([points[counter], np.ones_like(points[counter][0, :])]))
    uv[counter] = uv[counter] / uv[counter][2, :]
    counter += 1

"""
" This is a trial for just 1 image  "
path=str(identifier[0]) + str('\\')    
for infile in glob.glob(os.path.join(path,"*cloud.bin") ):
    points.append((load_pc_from_bin(infile)));
        
for infile in glob.glob(os.path.join(path,"*proj.bin") ):
    camera.append(load_pc_from_bin(infile));
    
uv.append(camera[counter] @ np.vstack([points[counter], np.ones_like(points[counter][0, :])]))
uv[counter] = uv[counter] / uv[counter][2, :]
" Ends here "
"""



" Find projected 3D points within bounds of 2D box & select as array"
bbox_2D_indexes=[]
counter=0;
for uv_i in uv:
    temp_points=[]
    temp_indexes=[]
    for j in range(len(uv_i.T)):
        if (float(uv_i[0,j]) > (float(bbox_x[counter])-float(bbox_w[counter])/2) 
            and float(uv_i[0,j]) < (float(bbox_x[counter])+float(bbox_w[counter])/2)
            and float(uv_i[1,j]) > (float(bbox_y[counter])-float(bbox_h[counter])/2) 
            and float(uv_i[1,j]) < (float(bbox_y[counter])+float(bbox_h[counter])/2)):
            temp_points.append(uv_i[:,j])
            temp_indexes.append(j)
        
    bbox_2D_indexes.append(temp_indexes)
    
    counter += 1;
center_3D_x=[]
center_3D_y=[]
center_3D_z=[]
r=[]
theta=[]
volume=[]
width=[]
height=[]
depth=[]
counter = 0;

for image in points:
    if not bbox_2D_indexes[counter]:
        print("Empty list")
        center_3D_x.append(0)
        center_3D_y.append(0)
        center_3D_z.append(0)
        r.append(0)
        theta.append(0)
        volume.append(0)
        width.append(0)
        height.append(0)
        depth.append(0)
    else:
        temp_index=np.asarray(bbox_2D_indexes[counter]).reshape((1, -1)).astype(int);
        center_3D_x.append(np.mean(points[counter][0,temp_index]))
        center_3D_y.append(np.mean(points[counter][1,temp_index]))
        center_3D_z.append(np.mean(points[counter][2,temp_index]))    
        Cum_x=0.0
        Cum_y=0.0
        Cum_z=0.0
        mean_counter=0
        new_indexes=[]
        
        
        for ii in range(len(temp_index.T)):
            if (points[counter][2,temp_index[0,ii]] < center_3D_z[counter]*1.05):
                Cum_x += points[counter][0,temp_index[0,ii]]
                Cum_y += points[counter][1,temp_index[0,ii]]
                Cum_z += points[counter][2,temp_index[0,ii]]
                new_indexes.append(temp_index[0,ii])
                mean_counter += 1;
    
    
        center_3D_x[counter]=Cum_x/mean_counter
        center_3D_y[counter]=Cum_y/mean_counter
        center_3D_z[counter]=Cum_z/mean_counter
    
        "Find r and theta and volume for bounding box"
        width.append(np.ptp(points[counter][0,new_indexes]))
        height.append(np.ptp(points[counter][1,new_indexes]))
        depth.append(np.ptp(points[counter][2,new_indexes]))
        r.append(np.power((np.power(center_3D_x[counter],2) + np.power(center_3D_y[counter],2) + np.power(center_3D_z[counter],2)),0.5))
        theta.append(np.arctan2(center_3D_x[counter],center_3D_z[counter]))
        volume.append(width[counter]*height[counter]*depth[counter])
    
    output = open('D:\\Team 2 - Knights\\3dbbox\\r599-detection-3d-bbox.txt','a')
    output.write(str(rr_path[counter]))
    output.write(",")
    output.write(str(classes[counter]))
    output.write(",")
    output.write(str(center_3D_x[counter]))
    output.write(",")
    output.write(str(center_3D_y[counter]))
    output.write(",")
    output.write(str(center_3D_z[counter]))
    output.write(",")
    output.write(str(depth[counter]))
    output.write(",")
    output.write(str(width[counter]))
    output.write(",")
    output.write(str(height[counter]))
    output.write(",")
    output.write(str(bbox_conf[counter]))
    output.write("\n")
    output.close()
    counter += 1;

raw_data.close()



