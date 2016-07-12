#coding: utf-8

import os
import Image


path=os.path.join('E:\\','places')
#path=os.path.join('E:\\','places_copy')
#path=os.path.join('E:\\','places','a','机舱')


def printdir(path):
    for fileName in os.listdir(path):
        abs_path=os.path.join(path,fileName)
        if os.path.isdir(abs_path):
            
            if os.path.split(abs_path)[1]=='b' or os.path.split(abs_path)[1]=='a' or os.path.split(abs_path)[1]=='c' or os.path.split(abs_path)[1]=='d' or os.path.split(abs_path)[1]=='e' :
                
                pass
            else:
                print abs_path
                printdir(abs_path)
        else:
            if os.path.splitext(fileName)[1]=='.jpg':
                
                abs_path=os.path.join(path,fileName)
                new_fileName='out_'+os.path.split(fileName)[1]
                try:
                    im=Image.open(abs_path)
                    (x,y)=im.size
                    if x==256 and y==256:
                        pass
                    else:
                        print 'yes'
                        im=im.resize((256,256))
                        print os.path.join(path, new_fileName)
                        im.save(os.path.join(path,new_fileName),'jpeg')
                        os.remove(abs_path)
                except:
                    os.remove(abs_path)
                    pass
printdir(path)
