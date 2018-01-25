import os

root_path = "D:\\Team 2 - Knights\\3dbbox\\"
file_name = "r599-detection.txt"
new_file_name = "r599-detection-v2.txt"

path = os.path.join(root_path, file_name)
new_path = os.path.join(root_path, new_file_name)

new_file = open(new_path, "a") 
with open(path, "r+") as file:
    for line in file:
        line = line.replace("testimages","test")
        new_file.write(line)
new_file.close()