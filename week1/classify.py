import os
import Image
import pdb

scenefilename=os.path.join('C:\Users\space\Desktop\mywork\scenes_work','scene_label.txt')
filename=os.path.join('C:\Users\space\Desktop\mywork\scenes_work','classes1.txt')
name=[]
label_id=[]


with open(scenefilename,'r') as f:
    lines=f.readlines()

ids=[line.strip().split(';')[0] for line in lines]
character=[line.strip().split(';')[1] for line in lines]
labels_ids=dict(map(lambda x,y:[x,y], ids,character))

for c in character:
    with open(filename,'a') as f1:
        f1.write(c+'\n')

