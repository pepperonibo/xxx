import os

# 调参直接到cmd中改

# root_path = os.path.dirname(__file__)
root_path = os.path.abspath(".")
class_list = os.listdir(os.path.join(root_path,"samples"))
print(class_list)

os.chdir(os.path.join(root_path,"training_set"))
print(os.getcwd())

for item in class_list:
    cmd = "opencv_traincascade.exe -data " + item + " -vec " + item + ".vec -bg " + item + "_neg.txt -numPos 5 -numNeg 70 -numStages 5 -w 60 -h 60 -minHitRate 0.999 -maxFalseAlarmRate 0.2 -weightTrimRate 0.95 -featureType LBP"
    print(cmd)
    os.system(cmd)