import os

def convert_path(path: str) -> str:
    seps = r'\/'
    sep_other = seps.replace(os.sep, '')
    return path.replace(sep_other, os.sep) if sep_other in path else path

root_path = os.path.dirname(__file__)
# root_path = os.path.abspath(".")
list_samples_dir = os.listdir(os.path.join(root_path,"samples"))
list_pos_samples = []

for item in list_samples_dir:
    temp_path = root_path + "/samples/" + item + "/resized_pics"
    list_pos_samples.append(convert_path(temp_path))

# print(list_pos_samples)

pos_text_list = []

for item in list_pos_samples:
    pos_text_list.append(item.capitalize() + "\pos.txt")
    cmd = "dir /s/b " + item.capitalize() + " > " + item.capitalize() + "\pos.txt"
    print(cmd)
    os.system(cmd)

with open("./pos_path.txt","w") as f:
    for item in pos_text_list:
        f.write(item + "\n")