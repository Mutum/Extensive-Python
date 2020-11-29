"""convert to jpg"""

import os
from PIL import Image
import io
import pathlib
import argparse


def p2j(path,file_name):
    path = path
    try:
        im = Image.open(pathlib.Path(path, str(file_name +".png")),'r')
        im.save(str(file_name +"jpg" +".jpg"))
    except:
        return print(f'image is not png file ')
        
        
# p2j(path = "D:\Courses\EPAI\session_11\project\Assignment",file_name ="orchid1")

if __name__ == '__main__':
    print('running jpg_conversion ......')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path',
                        type=str, help='the path of the image.')
    parser.add_argument('image_name',
                        type=str, help='the image name')
    args = parser.parse_args()
    print(f'png conversion: {args.path}\{args.image_name}')
    p2j(path=str(args.path), file_name=args.image_name)
    