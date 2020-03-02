import os

final_size = " 60 60"
Neg_Size_Per_Class = 11

pos_list = []
pos_list_string = ""
# root_path = os.path.dirname(__file__)
root_path = os.path.abspath(".")

with open("./pos_path.txt","r") as f:
    pos_list_string = f.read()

pos_list = pos_list_string.split("\n")
pos_list = pos_list[:-1]
# print(pos_list)
class_list = os.listdir(os.path.join(root_path,"samples"))

def mk_train_dir():
    try:
        os.mkdir("training_set")
    except FileExistsError:
        print("direction has been exsited")

def read_content(pos_url):
    temp_pos = ""
    with open(pos_url,"r") as f:
        temp_pos = f.read()
    temp_pos_content = temp_pos.split("\n")
    return temp_pos_content[:-2]

    
if __name__ == "__main__":
    mk_train_dir()
    neg_list = []
    # 获取正实例
    for i in range(len(class_list)):
        format_content_list = []
        content = read_content(pos_list[i])
        for item in content:
            format_content_list.append(item + " 1 0 0" + final_size)
        with open("./training_set/" + class_list[i] + ".txt","w") as f:
            f.write("\n".join(format_content_list))
    # 获取负实例
        # neg_list.extend(format_content_list)
        neg_list.extend(content)
    for i in range(len(class_list)):
        temp_neg = neg_list[:i * Neg_Size_Per_Class] + neg_list[(i + 1) * Neg_Size_Per_Class:]
        with open("./training_set/" + class_list[i] + "_neg.txt","w") as f:
            f.write("\n".join(temp_neg))