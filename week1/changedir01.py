import os
import Image
import pdb

scenefilename=os.path.join('C:\\Users\\Administrator\\Desktop\\scenes_work','scenes_labels.txt')
name=[]
label_id=[]


with open(scenefilename,'r') as f:
    lines=f.readlines()
labels=[os.path.join(u'E:\\thunder_download\\data_256',line.strip().split()[0].replace('/','\\')[1:]) for line in lines]
ids=[line.strip().split()[1] for line in lines]
labels_ids=dict(map(lambda x,y:[x,y], labels,ids))
path=os.path.join('E:\\','thunder_download','data_256')


def changedir(path):
   
    for fileName in os.listdir(path):
        abs_path=os.path.join(path,fileName)
        print abs_path
        if os.path.isdir(abs_path):
                print abs_path
                changedir(abs_path)
        else:
           new_file_prex=labels_ids[path]
           new_file=os.path.join('E:\\thunder_download\\places365standard_256_train',new_file_prex)
           isExist=os.path.exists(new_file)
           if not isExist:
               os.mkdir(new_file)
           else:
               pass   
           new_filename=os.path.join(new_file,fileName)
           print new_filename
           os.rename(abs_path,new_filename)
changedir(path)

