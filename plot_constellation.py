# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import os

def get_coordinate(file):
    x=[]
    y=[]
    with open(file) as f:
        for line in f.readlines():
            a = line.split(':')[1]
            a = a.split(' ')[0]
            b = line.split(':')[2]
            a = float(a)
            b = float(b)
            if not (a==0 and b==0):
                x.append(a)
                y.append(b)
    return [x,y]

def get_img(file):
    dir_aim, file_aim = file.rsplit("\\", 1)
    new_folder = dir_aim + '\\' +  'img\\'
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    # print(dir_aim,file_aim)
    x,y=get_coordinate(file)
    fig = plt.figure(figsize=(6, 4)).add_subplot(111,facecolor='#000000')
    fig.scatter(x,y,s=5,c='#00FF00',norm=1,marker='o')
    fig.set_title(file_aim.split('.')[0])
    # fig.set_xlabel('This is x axis')
    # fig.set_ylabel('This is y axis')
    plt.savefig(new_folder+file_aim.split('.')[0]+'.jpg')

#test
# get_img(r'C:\Users\81510\Desktop\pucch_data.log')
# x1,y1=get_coordinate(r'C:\Users\81510\Desktop\pucch_data.log')
