#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def RRC_manage(file):
    RIB={'ue_identity':[],'eea':None,'eia':None,'PHY_time':0,'mean_cfo':0,'mean_rsrp':0,'RRC_connect_time':[],
         'RRC_reconfiguration_time':[],'pci':[],'dl_earfcn':[],'cell_id':[],} #使用一个字典存储读取的RRC信息 RRC Information Block
    #pci 物理小区标识 dl_earfcn频点号

    with open(file,'rb') as f:
        cfo = []
        rsrp = []
        for line in f.readlines():
            line=line.decode()
            if 'New measurement serving cell' in line and 'cfo' in line:
                tmp_list=re.findall(r"-?\d+\.?\d*", line)
                tmp_rsrp=float(tmp_list[-2])
                tmp_cfo=float(tmp_list[-1])
                cfo.append(tmp_cfo)
                rsrp.append(tmp_rsrp)
            elif 'ue-Identity' in line:
                position=line.find('0x')
                if line[position:-2] not in RIB['ue_identity']:
                    RIB['ue_identity'].append(line[position:-2])
            elif 'eea' in line and 'eia' in line:
                p_eea=line.find('eea:')
                p_eia=line.find('eia:')
                RIB['eea']=line[p_eea+5:p_eea+9]
                RIB['eia']=line[p_eia+5:-2]
            elif 'Starting PLMN search' in line:
                PHY_start=float(line[6:15])
            elif 'FSM "selecting_cell"' in line and 'successfully selected' in line:
                PHY_end = float(line[6:15])
                phy_time = ("%.6f" % (PHY_end-PHY_start))
                RIB['PHY_time']=phy_time
            elif 'rrcConnectionRequest' in line:
                rrcConnection_start = float(line[6:15])
            elif 'rrcConnectionSetupComplete' in line:
                rrcConnection_end=float(line[6:15])
                RIB['RRC_connect_time'].append("%.6f" % (rrcConnection_end-rrcConnection_start))
            elif 'Rx rrcConnectionReconfiguration' in line:
                rrcReconfiguration_start = float(line[6:15])
            elif 'Tx rrcConnectionReconfigurationComplete' in line:
                rrcReconfiguration_end=float(line[6:15])
                RIB['RRC_reconfiguration_time'].append("%.6f" % (rrcReconfiguration_end-rrcReconfiguration_start))
            elif 'pci:' in line and 'cell_id:' in line:
                tmp_list = re.findall(r"-?\d+\.?\d*", line)
                tmp_dlearfcn=tmp_list[-3]
                tmp_pci=tmp_list[-4]
                if tmp_dlearfcn not in RIB['dl_earfcn']:
                    RIB['dl_earfcn'].append(tmp_dlearfcn)
                if tmp_pci not in RIB['pci']:
                    RIB['pci'].append(tmp_pci)
                tmp_list = re.findall(r"0x\w+", line) #匹配0x
                if tmp_list[0] not in RIB['cell_id'] and tmp_list[0]!='0x0':
                    RIB['cell_id'].append(tmp_list[0])
        mean_cfo=sum(cfo)/len(cfo)
        mean_rsrp=sum(rsrp)/len(rsrp)
        RIB['mean_cfo']=("%.2f Hz" % (mean_cfo))
        RIB['mean_rsrp'] = ("%.2f dBm" % (mean_rsrp))
    return RIB

print(RRC_manage(r'C:\Users\81510\Desktop\RRC.log'))