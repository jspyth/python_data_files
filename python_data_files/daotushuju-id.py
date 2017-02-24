#coding=utf-8
##
import pprint
import re
import os
import linecache
#import numpy as np

subGraphID = '4582'
nodeFileName = '../raw/car_person_node.txt'
edgeFileName = '../raw/car_person_edge.txt'
newFileName = './man_car.csv'

Monthl=[]
nodefopen = open(nodeFileName, 'rt')
edgefopen = open(edgeFileName, 'rt')
for line in edgefopen:
    if(line.split('\t')[3].strip() == subGraphID):
        time = line.split('\t')[2].split(' ')[0]
        key = time[0:7]               # first 7 elements are the key of the dict, get it and append the relevent data to it.
        source = line.split('\t')[0]
        target = line.split('\t')[1]
        Monthl.append(source)
        Monthl.append(target)
edgefopen.close()

out = []
nodeIndex = Monthl#将所有node id存入nodeIndex数组
nodeInfo = []
isCar = []    #判断节点的类型
linecache.clearcache()
for j in nodeIndex:
    line = linecache.getline(nodeFileName,int(j)+1) # 节点ID和行数的对应关系，行数 = ID + 1，从点文件获取行
    nodeInfo.append(line.split('\t')[2])# 从点文件获取的行里选中所挑出的项
    isCar.append(line.split('\t')[1])     # 1是car，2是person

i=0

edgefopen = open(edgeFileName, 'rt')
for line in edgefopen:#此处循环次数为总行数
    if(line.split('\t')[3].strip() == subGraphID):  #找到符合目的的子图
        if (i/2==0) or (i%2==0):
            item='"'+nodeInfo[i]+'","'+nodeInfo[i+1]+'",'# 取ID号和牌号
            x1=line.split('\t')[2].split(' ')[0].split('-')[1]#取月份
            x2=line.split('\t')[2].split(' ')[0].split('-')[2]#取日期
            x3=line.split('\t')[2].split(' ')[1].split(':')[0]#取小时
            x4=line.split('\t')[2].split(' ')[1].split(':')[1]#取分
            x5=line.split('\t')[2].split(' ')[1].split(':')[2]#取秒
            item2=x1+','+x2+','+x3+','+x4+','+x5
            item3=line.split('\t')[0].strip()+','+line.split('\t')[1].strip()+','
            i=i+2
            out.append(item3+item+item2)
                   
edgefopen.close()
#写入设置文件
fopen = open(newFileName, 'w')
for line in out:
    fopen.write(line)
    fopen.write('\n')
fopen.close();
print('---TASK IS OVER---')
