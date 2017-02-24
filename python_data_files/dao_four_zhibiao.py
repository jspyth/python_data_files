#coding=utf-8
# 该程序用于把四个指标数据文件中的指标数据导入一个文件中，并修改为csv格式

import json 
import csv
import re
import os

nodeFileName_one = 'result_degree-haitun.txt'
nodeFileName_two = 'result_slc-haitun.txt'
nodeFileName_three = 'result_bc-haitun.txt'
nodeFileName_four = 'result_cc-haitun.txt'
newFileName = 'four_zhibiao.csv'

data = []
nodeNum = 0
nodefopen_one = open(nodeFileName_one, 'rt')
nodefopen_two = open(nodeFileName_two, 'rt')
nodefopen_three = open(nodeFileName_three, 'rt')
nodefopen_four = open(nodeFileName_four, 'rt')

firstline = 'id'+','+'degree'+','+'slc'+','+'bc'+','+'cc'
data.append(firstline)
for line in nodefopen_one:
	Id=line.split('\t')[0].strip()
	degree=line.split('\t')[1].strip()
	for line in nodefopen_two:
		slc=line.split('\t')[1].strip()
		for line in nodefopen_three:
			bc=line.split('\t')[1].strip()
			for line in nodefopen_four:
				cc=line.split('\t')[1].strip()
				newline =Id+','+degree+','+slc+','+bc+','+cc
				data.append(newline)
				nodeNum += 1
				print (nodeNum)
				break
			break
		break

nodefopen_one.close()
nodefopen_two.close()
nodefopen_three.close()
nodefopen_four.close()

fopen = open(newFileName,"w")
for line in data:
    fopen.write(line)
    fopen.write('\n')
fopen.close()
print('Task is over!')