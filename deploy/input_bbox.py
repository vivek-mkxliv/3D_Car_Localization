from glob import glob
import numpy as np
import os

train_dir = "C:\\Users\\vivek\\Desktop\\V\\UMich\\S3 - Fall 2017\\ROB 599\\Project\\Perception_v2\\deploy\\trainval\\"

def rot(n, theta):
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return np.identity(3) + np.sin(theta) * K + (1 - np.cos(theta)) * K @ K

def get_bbox(p0, p1):
    '''
    Input:
    *   p0, p1
        (3)
        Corners of a bounding box represented in the body frame.
    Output:
    *   v
        (3, 8)
        Vertices of the bounding box represented in the body frame.
    *   e
        (2, 14)
        Edges of the bounding box. The first 2 edges indicate the `front` side
        of the box.
    '''
    v = np.array([[p0[0], p0[0], p0[0], p0[0], p1[0], p1[0], p1[0], p1[0]],
                  [p0[1], p0[1], p1[1], p1[1], p0[1], p0[1], p1[1], p1[1]],
                  [p0[2], p1[2], p0[2], p1[2], p0[2], p1[2], p0[2], p1[2]]])
    e = np.array([[2, 3, 0, 0, 3, 3, 0, 1, 2, 3, 4, 4, 7, 7],
                  [7, 6, 1, 2, 1, 2, 4, 5, 6, 7, 5, 6, 5, 6]], dtype=np.uint8)

    return v, e

for folder in os.listdir(train_dir):
    if os.path.isdir(os.path.join(train_dir,folder)):
        path = os.path.join(train_dir,folder)
        images = glob(path+'/*_image.jpg') 
        labels = []
        for image in images:
            name_list = image.split("/")
            name_list[-1] = name_list[-1].replace(".jpg",".txt")
            label = "/".join(name_list)
            name_list[-1] = name_list[-1].replace("_image.txt","_bbox.bin")
            bbox = "/".join(name_list)
            name_list[-1] = name_list[-1].replace("_bbox.bin","_proj.bin")
            proj = "/".join(name_list)
            name_list[-1] = name_list[-1].replace("_proj.bin", "_cloud.bin")
            cloud = "/".join(name_list)
            numpy_proj = np.fromfile(proj,dtype=np.float32)
            numpy_bbox = np.fromfile(bbox,dtype=np.float32)
            numpy_cloud = np.fromfile(cloud,dtype=np.float32)
            numpy_cloud.resize([3, numpy_cloud.size // 3])
            numpy_proj.resize([3, 4])
            numpy_bbox.resize([numpy_bbox.size // 11, 11])
            uv = numpy_proj @ np.vstack([numpy_cloud, np.ones_like(numpy_cloud[0, :])])
            uv = uv / uv[2, :]
            label_file = open(label,"w")
            for k, b in enumerate(numpy_bbox):
                vertex_list = []
                n = b[0:3]
                theta = np.linalg.norm(n)
                n /= theta
                R = rot(n, theta)
                t = b[3:6]

                sz = b[6:9]
                vert_3D, edges = get_bbox(-sz / 2, sz / 2)
                vert_3D = R @ vert_3D + t[:, np.newaxis]

                vert_2D = numpy_proj @ np.vstack([vert_3D, np.ones(8)])
                vert_2D = vert_2D / vert_2D[2, :]
                point_new_array = np.array([])
            #This is the code for creating the list of (x,y) points for the one bbox of image so that you can work on the getting 
            #4 points out of it.     
                for e in edges.T:
                    x_points = [np.asscalar(x) for x in np.expand_dims(vert_2D[0,e], axis=1)]
                    y_points = [np.asscalar(x) for x in np.expand_dims(vert_2D[1,e], axis=1)]
                    point = list(zip(x_points, y_points))
                    vertex_list.append(point[0])
            #         point = np.concatenate((np.expand_dims(vert_2D[0,e], axis=1), np.expand_dims(vert_2D[1,e], axis=1)), axis=1)
            #         point_new_array = np.concatenate((point_new_array, point))
                vertex_list = list(set(vertex_list))
                x_list = sorted(vertex_list)
                y_list = sorted(vertex_list, key=lambda arg: arg[1])
                x_min = x_list[0][0]
                x_max = x_list[-1][0]
                y_min = y_list[0][1]
                y_max = y_list[-1][1]
                centroid = []
                centroid.append((x_min+x_max)/2)
                centroid.append((y_min+y_max)/2)
                n = 1052
                m = 1914
                if centroid[0]<m and centroid[1]<n and centroid[0]>0 and centroid[1]>0:
                    w = (x_max-x_min)
                    h = (y_max-y_min)
                    centroid[0] = centroid[0]/m
                    centroid[1] = centroid[1]/n
                    w = abs(w)/m
                    h = abs(h)/n
                    c = int(b[9])
                    message = str(c)+" "+str(centroid[0])+" "+str(centroid[1])+" "+str(w)+" "+str(h)+"\n"
                    label_file.write(message)
            label_file.close()