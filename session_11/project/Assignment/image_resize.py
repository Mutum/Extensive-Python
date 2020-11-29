# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:29:25 2020

@author: Mutum
"""
import os
from PIL import Image
import io
import pathlib

Image.open(r'D:\Courses\EPAI\session_11\project\Assignment\orchid1.jpg')

im = Image.open(r'D:\Courses\EPAI\session_11\project\Assignment\orchid1.jpg')
im.width
    

def res_p(path,file_name,resize_percentage=1):
    path = path
    try:
        im = Image.open(pathlib.Path(path, str(file_name +".jpg")),'r')
        (width, height) = (im.width * resize_percentage, im.height *resize_percentage)
        newsize = (width, height) 
        im1 = im.resize(newsize)
        im1.save(str(file_name +"resize" +".jpg"))
    except:
        im = Image.open(pathlib.Path(path, str(file_name +".png")),'r')
        (width, height) = (im.width * resize_percentage, im.height *resize_percentage)
        # im.save(str(file_name +"resize" +".png"))
        newsize = (width, height) 
        im1 = im.resize(newsize)
        im1.save(str(file_name +"resize" +".png"))
    finally:
        return print(f'only png and jpg file works')
       
res_p(path = "D:\Courses\EPAI\session_11\project\Assignment",file_name ="orchid1png")


def res_w(path,file_name,width= None):
    path = path
    
    try:
        im = Image.open(pathlib.Path(path, str(file_name +".jpg")),'r')
        width = width
        if width == None:
            width = im.width
        (width, height) = (width, im.height)
        newsize = (width, height) 
        im1 = im.resize(newsize)
        im1.save(str(file_name +"width_change" +".jpg"))
    except:
        im = Image.open(pathlib.Path(path, str(file_name +".png")),'r')
        width = width
        if width == None:
            width = im.width
        (width, height) = (width, im.height)
        # im.save(str(file_name +"resize" +".png"))
        newsize = (width, height) 
        im1 = im.resize(newsize)
        im1.save(str(file_name +"width_change" +".png"))
    finally:
        return print(f'only png and jpg file works')
    

def res_h(path,file_name,height=None):
    path = path
    try:
        im = Image.open(pathlib.Path(path, str(file_name +".jpg")),'r')
        height = height
        if height == None:
            height = im.height
        (width, height) = (im.width,height)
        newsize = (width, height) 
        im1 = im.resize(newsize)
        im1.save(str(file_name +"height_change" +".jpg"))
    except:
        im = Image.open(pathlib.Path(path, str(file_name +".png")),'r')
        (width, height) = (im.width, height)
        # im.save(str(file_name +"resize" +".png"))
        newsize = (width, height) 
        im1 = im.resize(newsize)
        im1.save(str(file_name +"height_change" +".png"))
    finally:
        return print(f'only png and jpg file works')
    
res_h(path = "D:\Courses\EPAI\session_11\project\Assignment",file_name ="orchid1",
      height = 250)




