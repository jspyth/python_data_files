#coding=utf-8
##

import json 
import csv
import re
import os

nodeFileName = 'result_degree.txt';# 这个文件替换成带有排序好的id的文件即可，每行一个id
newFileName = 'json.json'# 这是最终的json文件
data = []
nodeNum = 71 # 要事先给出结点数目，这里是0~70共71个
edgeNum = 686 # 要事先给出边数目，看边文件行数
a = 0# 中间变量
b = 0# 中间变量 
nodefopen = open(nodeFileName, 'rt');

data.append('{')
data.append('\"nodes\":[')
for line in nodefopen:
        Id=line.split('\t')[0].strip()
        a += 1
        if a<= (nodeNum - 1):
            newline ='{'+'\n'+'\"id\":'+Id+'\n'+'},'
        else:
            newline ='{'+'\n'+'\"id\":'+Id+'\n'+'}'# 按照json的格式最后一个要去掉逗号
        data.append(newline)
data.append('],')
nodefopen.close()

edgeFileName = './output.txt'# 这个是边文件
edgefopen = open(edgeFileName, 'rt')
data.append('\"links\":[')
for line in edgefopen:
    source=line.split('\t')[0].strip()
    target=line.split('\t')[1].strip()
    b+= 1
    print(b)
    if b <= (edgeNum - 1):
        newLine='{'+'\n'+'\"source\":'+source+',\n'+'\"target\":'+target+'\n'+'},'
        data.append(newLine)
    else:
        newLine='{'+'\n'+'\"source\":'+source+',\n'+'\"target\":'+target+'\n'+'}'# 按照json的格式最后一个要去掉逗号
        data.append(newLine)

data.append(']')
data.append('}')
edgefopen.close()
#print '---TASK IS OVER---'

fopen = open(newFileName,"w");
for line in data:
    fopen.write(line)
    fopen.write('\n')
fopen.close();


