# -*- coding: utf-8 -*-
"""
convert to png
"""
import os
from PIL import Image
import io
import pathlib

Image.open(r'D:\Courses\EPAI\session_11\project\Assignment\orchid1.jpg')
# im1.save(r'path where the PNG will be stored\new file name.png')

# Image.open(r'D:\Courses\EPAI\session_11\project\Assignment\orchid2.jpeg')

# def j2p(path,file_name):
#     try:
#         path = os.path.join(path, file_name,".jpeg")
#         im =Image.open(r'D:\Courses\EPAI\session_11\project\Assignment\orchid1.jpeg')
#         im.save('orchid1.png')
#     except:
#         im =Image.open(r'D:\Courses\EPAI\session_11\project\Assignment\orchid1.jpg')
#         im.save('orchid1.png')
        

# path = os.path.join('D:\Courses\EPAI\session_11\project\Assignment')


# Image.open(pathlib.Path(path, str("orchid1"+".jpg")),'r')

# Image.open(r'D:\Courses\EPAI\session_11\project\Assignment\orchid1.jpg')


def j2p(path,file_name):
    path = path
    try:
        im = Image.open(pathlib.Path(path, str(file_name +".jpeg")),'r')
        im.save(str(file_name +"png" +".png"))
    except:
        im = Image.open(pathlib.Path(path, str(file_name +".jpg")),'r')
        im.save(str(file_name +"png" +".png"))
        
        
# j2p(path = "D:\Courses\EPAI\session_11\project\Assignment",file_name ="orchid1")
