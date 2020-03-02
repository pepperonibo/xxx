from PIL import Image
import os

# root_path = os.path.abspath(".")
root_path = os.path.dirname(__file__)
final_size = (60,60)

def Image_resize(pic_path,new_pic_path):
    im = Image.open(pic_path)
    # print("image mode" + im.mode)
    if im.mode == "P":
        if "transparency" in im.info:
            im = im.convert('RBGA')
        else:
            im = im.convert('RGB')
    if im.mode == "RGBA":
        out = Image.new("RGB", im.size, (255,255,255))
        out.paste(im,mask=im)
    else:
        out = im
    out = out.resize(final_size)
    out.save(new_pic_path)

def read_dir(cur_path):
    dir_list = os.listdir(os.path.join(root_path,cur_path))
    for item in dir_list:
        if os.path.isdir(os.path.join(root_path,cur_path,item)):
            read_dir(os.path.join(cur_path,item))
        elif item.endswith(".jpg"):
            try:
                os.mkdir(os.path.join(root_path,cur_path,"resized_pics"))
            except FileExistsError:
                print("direction has been existed")
            print(cur_path+item)
            Image_resize(os.path.join(root_path,cur_path,item),os.path.join(root_path,cur_path,"resized_pics",item))


if __name__ == "__main__":
    read_dir("")