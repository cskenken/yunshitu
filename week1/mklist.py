import os
import Image
import pdb

scenefilename=os.path.join('/data/disk3/faster_rcnn_train','scene_label.txt')
filename=os.path.join('/data/disk3/faster_rcnn_train','path_label.txt')
name=[]
label_id=[]


with open(scenefilename,'r') as f:
    lines=f.readlines()

ids=[line.strip().split(';')[0] for line in lines]
character=[line.strip().split(';')[1] for line in lines]
labels_ids=dict(map(lambda x,y:[x,y], ids,character))
path='/data/disk3/faster_rcnn_train/scene_data'



def makedir(path):
    
    for fileName in os.listdir(path):
        abs_path=os.path.join(path,fileName)
        print abs_path
        if os.path.isdir(abs_path):
                print abs_path
                makedir(abs_path)
        else:
           print path
           last=os.path.split(path)[1]
           print last
           label=labels_ids[last]
           with open(filename,'a') as f1:
               f1.write(abs_path+' '+label+'\n')
           
           
makedir(path)
