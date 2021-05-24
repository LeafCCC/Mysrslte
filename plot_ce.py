#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import matplotlib.pyplot as plt

def get_ce_coordinate(file):
    x = np.arange(1, 769, 1)
    y = [0.0] * 768
    with open(file) as f:
        i = 0
        for line in f.readlines():
            a = line.split(':')[1]
            a = a.split(' ')[0]
            a = float(a)
            if a != -80:
                y[i]=y[i] - a
            if i != 767:
                i += 1
            else:
                i = 0
    return [x,y]

def get_ce_img(file):
    x,y=get_ce_coordinate(file)
    dir_aim, file_aim = file.rsplit("\\", 1)
    new_folder = dir_aim + '\\' + 'img\\'
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    plt.plot(x, y, label="ce_abs")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()

    plt.savefig(new_folder + file_aim.split('.')[0] + '.jpg')

# get_ce_img(r'C:\Users\81510\Desktop\log\enb_ce.log')











