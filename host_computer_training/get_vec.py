import os

root_path = os.path.dirname(__file__)
class_list = os.listdir(os.path.join(root_path,"samples"))
print(class_list)

os.chdir(os.path.join(root_path,"training_set"))

# 循环将txt转换成vec
for item in class_list:
    cmd = "opencv_createsamples.exe -vec " + item + ".vec -info " + item + ".txt -num 11 -w 60 -h 60"
    os.system(cmd)