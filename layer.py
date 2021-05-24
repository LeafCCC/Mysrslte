#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


list_ue=['NAS','PHY','MAC','RLC','PDCP','RRC','GW','STCK','UE','RF','USIM']
list_enb=['PHY','MAC','RLC','PDCP','RRC','ENB','S1AP','GTPU','RF','STCK']


#处理各层数据
def layer_manage(f1,dir,layer):
    tmp=0
    with open(dir+layer+'.log', 'a') as f2:
                for line in f1.readlines():
                    if '[%s' % layer in line:
                        tmp=1
                        f2.write(line)
                    elif '[' in line:
                        tmp=0
                    if tmp==1 and '[' not in line:
                        f2.write(line)


def file_layering(dir,terminal):
    # with open(dir) as f1:
    dir_aim,file_aim=dir.rsplit("\\",1)
    new_folder=dir_aim+'\\'+file_aim.split('.')[0]+'_layered\\'
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    if terminal=='ue':
        for i in list_ue:
            with open(dir) as f1:
                layer_manage(f1,new_folder,i)
    elif terminal=='enb':
        for i in list_enb:
            with open(dir) as f1:
                layer_manage(f1,new_folder,i)
    else:
        raise IOError





