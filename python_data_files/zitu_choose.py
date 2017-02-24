#coding=utf-8

# 该程序设定需要查看的top几值，然后将该节点以及外面四层结点筛选出来并生成子图边txt和子图json文件
import json 
import csv
import re
import os

# 原始数据的边文件
nodeFileName = '../raw/edges1.txt'
# 筛选出的子图
newFileName1 = './zitu_id.txt'
# 子图id从0开始的映射表
newFileName2 = './map_text.txt'
# 子图映射过后的边文件
newFileName3 = './zitu_edges.txt'
# 子图json文件
newFileName4 = './zitu_json.json'
# 下面是四个指标数据文件
File_bc = './result_bc.txt'
File_cc = './result_cc.txt'
File_degree= './result_degree.txt'
File_slc = './result_slc.txt'

newline1 = ''
newline2 = ''
data = []
data1 = []
data2 = []
data3 = []
Share_node = []
query_id = []
same1 = 0
same2 = 0
Node_Max_Num = 150
node_count = 0
nodeNum = 0
edgeNum = 0
Edge = 0
TopNum = 5 # 高亮前5，这个值之后由前端输入
second_query_id = []
third_query_id = []
forth_query_id = []
All_id = []
result_bc = [] # 获取所有的bc值
result_cc = [] # 获取所有的cc值
result_degree = [] # 获取所有的degree值
result_slc = [] # 获取所有的slc值
nodeNum = 0
bc_top = [] # bc指标top指标值
cc_top = [] # cc指标top指标值
degree_top = [] # degree指标top指标值
slc_top = [] # slc指标top指标值
bc_id = [] # bc指标top id号
cc_id = [] # cc指标top id号
degree_id = [] # degree指标top id号
slc_id = [] # alc指标top id号

# 将bc指标数据保存在数组中并排序(降序)
zhibiaofopen = open(File_bc, 'rt')
for line in zhibiaofopen:
    x1 = int(line.split('\t')[0].strip())
    x2 = float(line.split('\t')[1].strip())
    result_bc.append(x2)
result_bc.sort(reverse = True)
#print(result_bc)
# 取bc指标top值
i = 0
for num in result_bc:
    bc_top.append(result_bc[i])
    i+=1
    if i >= TopNum:
        break
#print(bc_top)
zhibiaofopen.close()
number1 = 0
xc = 0
for stc in bc_top:
    if stc == bc_top[TopNum - 1]:
        number1+=1
#print(number1)
# 取bc指标top id值
zhibiaofopen = open(File_bc, 'rt')
for line in zhibiaofopen:
    x1 = int(line.split('\t')[0].strip())
    x2 = float(line.split('\t')[1].strip())
    for number in bc_top:
        if x2 >= bc_top[TopNum - 1]:
            if x2 == bc_top[TopNum - 1]:
                xc+=1
                if xc <= number1:
                    bc_id.append(x1)
            else:
                bc_id.append(x1)
            break
zhibiaofopen.close()
#print(bc_id)

# 将cc指标数据保存在数组中并排序（升序）
zhibiaofopen = open(File_cc, 'rt')
for line in zhibiaofopen:
    x1 = float(line.split('\t')[0].strip())
    x2 = float(line.split('\t')[1].strip())
    result_cc.append(x2)
result_cc.sort()
#print(result_cc)
# 取cc指标top值
i= 0
for num in result_cc:
    cc_top.append(result_cc[i])
    i+=1
    if i >= TopNum:
        break
#print(cc_top)
zhibiaofopen.close()
number1 = 0
xc = 0
for stc in cc_top:
    if stc == cc_top[TopNum - 1]:
        number1+=1
#print(number1)
# 取cc指标top id值
zhibiaofopen = open(File_cc, 'rt')
for line in zhibiaofopen:
    x1 = int(line.split('\t')[0].strip())
    x2 = float(line.split('\t')[1].strip())
    for number in cc_top:
        if x2 <= cc_top[TopNum - 1]:
            if x2 == cc_top[TopNum - 1]:
                xc+=1
                if xc <= number1:
                    cc_id.append(x1)
            else:
                cc_id.append(x1)
            break
zhibiaofopen.close()
#print(cc_id)

# 将degree指标数据保存在数组中并排序(降序)
zhibiaofopen = open(File_degree, 'rt')
for line in zhibiaofopen:
    x1 = int(line.split('\t')[0].strip())
    x2 = int(line.split('\t')[1].strip())
    result_degree.append(x2)
result_degree.sort(reverse = True)
#print(result_degree)
# 取degree指标top值
i= 0
for num in result_degree:
    degree_top.append(result_degree[i])
    i+=1
    if i >= TopNum:
        break
#print(degree_top)
zhibiaofopen.close()
number1 = 0
xc = 0
for stc in degree_top:
    if stc == degree_top[TopNum - 1]:
        number1+=1
#print(number1)
# 取degree指标top id值
zhibiaofopen = open(File_degree, 'rt')
for line in zhibiaofopen:
    x1 = int(line.split('\t')[0].strip())
    x2 = float(line.split('\t')[1].strip())
    for number in degree_top:
        if x2 >= degree_top[TopNum - 1]:
            if x2 == degree_top[TopNum - 1]:
                xc+=1
                if xc <= number1:
                    degree_id.append(x1)
            else:
                degree_id.append(x1)
            break
zhibiaofopen.close()
#print(degree_id)

# 将slc指标数据保存在数组中并排序(降序)
zhibiaofopen = open(File_slc, 'rt')
for line in zhibiaofopen:
    x1 = int(line.split('\t')[0].strip())
    x2 = int(line.split('\t')[1].strip())
    result_slc.append(x2)
result_slc.sort(reverse = True)
#print(result_slc)
# 取slc指标top值
i= 0
for num in result_slc:
    slc_top.append(result_slc[i])
    i+=1
    if i >= TopNum:
        break
#print(slc_top)
zhibiaofopen.close()
number1 = 0
xc = 0
for stc in slc_top:
    if stc == slc_top[TopNum - 1]:
        number1+=1
#print(number1)
# 取slc指标top id值
zhibiaofopen = open(File_slc, 'rt')
for line in zhibiaofopen:
    x1 = int(line.split('\t')[0].strip())
    x2 = float(line.split('\t')[1].strip())
    for number in slc_top:
        if x2 >= slc_top[TopNum - 1]:
            if x2 == slc_top[TopNum - 1]:
                xc+=1
                if xc <= number1:
                    slc_id.append(x1)
            else:
                slc_id.append(x1)
            break
zhibiaofopen.close()
#print(slc_id)
def Fiirst_floor_slc():
    for x in slc_id:
        query_id.append(x)

def Fiirst_floor_bc():
    for x in bc_id:
        query_id.append(x)

def Fiirst_floor_cc():
    for x in cc_id:
        query_id.append(x)

def Fiirst_floor_degree():
    for x in degree_id:
        query_id.append(x)
Fiirst_floor_degree()

# 获取第一层结点
for a_id in query_id:
    node_count+=1
    #print(node_count)
    if node_count <= Node_Max_Num:
        All_id.append(a_id)
    else:
        break

cx1 = 0
#获取第二层id
nodefopen = open(nodeFileName, 'rt')
print('第一层')
print(query_id)#打印第一层结点 
for line in nodefopen:
    x1 = int(line.split('\t')[0].strip())
    x2 = int(line.split('\t')[1].strip())
    x3 = line.split('\t')[0].strip()
    x4 = line.split('\t')[1].strip()
    #保存第二层结点id
    for id in query_id:
        if x1 == id:
            #过滤掉第一层
            for id in query_id:
                if x2 == id:
                    cx1+=1
            if cx1 == 0:
                #获取第二层结点
                second_query_id.append(x2)
            else:
                Share_node.append(x2)
                cx1 = 0
            #获取第一层结点和第二层结点之间的边到文本中
            newline = x3 + '\t' + x4
            data.append(newline)
        if x2 == id:
            #过滤掉第一层
            for id in query_id:
                if x1 == id:
                    cx1+=1
            if cx1 == 0:
                #获取第二层结点
                second_query_id.append(x1)
            else:
                Share_node.append(x1)
                cx1 = 0
            #获取第一层结点和第二层结点之间的边到文本中
            newline = x3 + '\t' + x4
            data.append(newline)
#数组去重
sec1 = set(second_query_id) 
sec_qu_chong_id = [ i for i in sec1]
#数组排序（升序）
sec_qu_chong_id.sort()
for a2 in sec_qu_chong_id:
    node_count+=1
    if node_count <= Node_Max_Num: # 如果结点数量超过限定值，不再保存结点 
        All_id.append(a2)
    else:
        break
print('第二层')
print(sec_qu_chong_id)#打印第二层结点 
nodefopen.close()# 必须先关闭，再打开

cx2 = 0
#获取第三层id
nodefopen = open(nodeFileName, 'rt');
for line in nodefopen:
    x1 = int(line.split('\t')[0].strip())
    x2 = int(line.split('\t')[1].strip())
    x3 = line.split('\t')[0].strip()
    x4 = line.split('\t')[1].strip()
    #保存第三层结点id
    for id1 in sec_qu_chong_id:
        if x1 == id1:
            #过滤掉第一层结点
            for x in query_id:
                if x2 == x:
                    same1 = same1 + 1
                    break
            if same1 == 0:
                #过滤掉第二层结点
                for id in sec_qu_chong_id:
                    if x2 == id:
                        cx1+=1
                if cx1 == 0:
                    #保存第三层结点id
                    third_query_id.append(x2)
                else:
                    Share_node.append(x2)
                    cx1 = 0
                #获取第二层结点和第三层结点之间的边到文本中
                newline = x3 + '\t' + x4
                data.append(newline)
            Share_node.append(x2)
            same1 = 0
        if x2 == id1:
            #过滤掉第一层结点
            for x in query_id:
                if x1 == x:
                    same2 = same2 + 1
                    break
            if same2 == 0:
                #过滤掉第二层结点
                for id in sec_qu_chong_id:
                    if x1 == id:
                        cx1+=1
                if cx1 == 0:
                    #保存第三层结点id
                    third_query_id.append(x1)
                else:
                    Share_node.append(x1)
                    cx1 = 0
                #获取第二层结点和第三层结点之间的边到文本中
                newline = x3 + '\t' + x4
                data.append(newline)
            Share_node.append(x1)
            same2 = 0
#数组去重
sec2 = set(third_query_id) 
third_qu_chong_id = [ j for j in sec2]
#数组排序（升序）
third_qu_chong_id.sort()
for a3 in third_qu_chong_id:
    node_count+=1
    if node_count <= Node_Max_Num: # 如果结点数量超过限定值，不再保存结点 
        All_id.append(a3)
    else:
        break
print('第三层')
print(third_qu_chong_id)#打印第三层结点 
nodefopen.close()

cx3 = 0
#获取第四层id
nodefopen = open(nodeFileName, 'rt')
for line in nodefopen:
    x1 = int(line.split('\t')[0].strip())
    x2 = int(line.split('\t')[1].strip())
    x3 = line.split('\t')[0].strip()
    x4 = line.split('\t')[1].strip()
    #保存第四层结点id
    for id2 in third_qu_chong_id:
        if x1 == id2:
            #过滤掉第二层结点
            for y in sec_qu_chong_id:
                if x2 == y:
                    same1 = same1 + 1
                    break
            if same1 == 0:
                #过滤掉第一层结点
                for id in query_id:
                    if x2 == id:
                        cx1+=1
                if cx1 == 0:
                    #过滤掉第三层结点
                    for id3 in third_qu_chong_id:
                        if x2 ==id3:
                            cx3+=1
                    if cx3 == 0:
                        #保存第四层结点id
                        forth_query_id.append(x2)
                    else:
                        Share_node.append(x2)
                        cx3 = 0
                else:
                    Share_node.append(x2)
                    cx1 = 0
                #获取第三层结点和第四层结点之间的边到文本中
                newline = x3 + '\t' + x4
                data.append(newline)
            Share_node.append(x2)
            same1 = 0
        if x2 == id2:
            #过滤掉第二层结点
            for y in sec_qu_chong_id:
                if x1 == y:
                    same2 = same2 + 1
                    break
            if same2 == 0:
                #过滤掉第一层结点
                for id in query_id:
                    if x1 == id:
                        cx1+=1
                if cx1 == 0:
                    #过滤掉第三层结点
                    for id3 in third_qu_chong_id:
                        if x1 ==id3:
                            cx3+=1
                    if cx3 == 0:
                        #保存第四层结点id
                        forth_query_id.append(x1)
                    else:
                        Share_node.append(x1)
                        cx3 = 0
                else:
                    Share_node.append(x1)
                    cx1 = 0
                newline = x3 + '\t' + x4
                data.append(newline)
            Share_node.append(x1)
            same2 = 0
#数组去重
sec2 = set(forth_query_id) 
forth_qu_chong_id = [ k for k in sec2]
#数组排序（升序）
forth_qu_chong_id.sort()
for a4 in forth_qu_chong_id:
    node_count+=1
    if node_count <= Node_Max_Num: # 如果结点数量超过限定值，不再保存结点 
        All_id.append(a4)
    else:
        break
print('第四层')
print(forth_qu_chong_id)#打印第四层结点 
#排序
All_id.sort()
#得到结点个数
list_len = len(All_id)

#对公共点进行去重
#sec2 = set(Share_node)
#share_qu_chong_node = [ k2 for k2 in sec2]
#for zhi in share_qu_chong_node:
    #All_id.append(zhi)
#sec3 = set(All_id)
#All_qu_chong_id = [ k3 for k3 in sec3]
#All_qu_chong_id.sort()
#nodefopen.close()

#创建出id映射表的数据以备保存到映射表中
def make_with_bcFile():
    for Index in range(0,len(All_id)):
        Index1 = str(Index)
        Id = str(All_id[Index])
        resultfopen = open(File_bc, 'rt')
        for line in resultfopen:
            x1 = int(line.split('\t')[0].strip())
            x2 = float(line.split('\t')[1].strip())
            x3= line.split('\t')[0].strip()
            x4 = line.split('\t')[1].strip()
            if int(Id) == x1:
                newline = Index1 + '\t' + Id + '\t' + x4
                data1.append(newline)
                break
        #print(Index,All_id[Index])
    print('所有子图结点')
    print(All_id)#打印出排序后的所有子图结点id
    resultfopen.close()

def make_with_ccFile():
    for Index in range(0,len(All_id)):
        Index1 = str(Index)
        Id = str(All_id[Index])
        resultfopen = open(File_cc, 'rt')
        for line in resultfopen:
            x1 = int(line.split('\t')[0].strip())
            x2 = float(line.split('\t')[1].strip())
            x3= line.split('\t')[0].strip()
            x4 = line.split('\t')[1].strip()
            if int(Id) == x1:
                newline = Index1 + '\t' + Id + '\t' + x4
                data1.append(newline)
                break
        #print(Index,All_id[Index])
    print('所有子图结点')
    print(All_id)#打印出排序后的所有子图结点id
    resultfopen.close()

def make_with_slcFile():
    for Index in range(0,len(All_id)):
        Index1 = str(Index)
        Id = str(All_id[Index])
        resultfopen = open(File_slc, 'rt')
        for line in resultfopen:
            x1 = int(line.split('\t')[0].strip())
            x2 = float(line.split('\t')[1].strip())
            x3= line.split('\t')[0].strip()
            x4 = line.split('\t')[1].strip()
            if int(Id) == x1:
                newline = Index1 + '\t' + Id + '\t' + x4
                data1.append(newline)
                break
        #print(Index,All_id[Index])
    print('所有子图结点')
    print(All_id)#打印出排序后的所有子图结点id
    resultfopen.close()

def make_with_degreeFile():
    for Index in range(0,len(All_id)):
        Index1 = str(Index)
        Id = str(All_id[Index])
        resultfopen = open(File_degree, 'rt')
        for line in resultfopen:
            x1 = int(line.split('\t')[0].strip())
            x2 = float(line.split('\t')[1].strip())
            x3= line.split('\t')[0].strip()
            x4 = line.split('\t')[1].strip()
            if int(Id) == x1:
                newline = Index1 + '\t' + Id + '\t' + x4
                data1.append(newline)
                break
        #print(Index,All_id[Index])
    print('所有子图结点')
    print(All_id)#打印出排序后的所有子图结点id
    resultfopen.close()

make_with_bcFile()

nodefopen.close()# 必须先关闭，再打开


#下面是保存子图的文件
fopen = open(newFileName1,"w")
for line in data:
    fopen.write(line)
    fopen.write('\n')
fopen.close();

#下面是保存id映射表，从0开始有利于生成json文件给前端可视化使用
fopen = open(newFileName2,"w");
for line in data1:
    fopen.write(line)
    fopen.write('\n')
fopen.close();


#下面是创建保存结点映射之后的子图边文件
nodefopen1 = open(newFileName1, 'rt'); 
for line in nodefopen1:
    x1 = int(line.split('\t')[0].strip())
    x2 = int(line.split('\t')[1].strip())
    xx1 = str(x1)
    xx2 = str(x2)
    nodefopen2 = open(newFileName2, 'rt'); 
    for line in nodefopen2:
        x3 = int(line.split('\t')[0].strip())
        x4 = int(line.split('\t')[1].strip())
        xx3 = str(x3)
        xx4 = str(x4)
        if x1 == x4:
            newline1 = xx3
        if x2 == x4:
            newline2 = xx3
    newline = newline1 + '\t' +newline2
    edgeNum = edgeNum + 1
    data2.append(newline)
    nodefopen2.close()
#把新的行读入新文件    
nodefopen1.close()
fopen = open(newFileName3,"w");
for line in data2:
    fopen.write(line)
    fopen.write('\n')
fopen.close();


#下面是创建子图的json文件
nodefopen = open(newFileName2, 'rt'); 
data3.append('{')
data3.append('\"nodes\":[')
for line in nodefopen:
    x1 = line.split('\t')[0].strip()
    x2 = line.split('\t')[2].strip()
    nodeNum = nodeNum + 1
    if nodeNum <= (list_len - 1):
        newline = '{' + '\n' + '\"id\":'+ x1 + ',' + '\n' + '\"result:\"'+x2+ '\n' + '},'
    else:
        newline = '{' + '\n' + '\"id\":'+ x1 + ',' + '\n' + '\"result\":' + x2+ '\n' + '}'
    data3.append(newline)
data3.append('],')
fopen.close();

edgefopen = open(newFileName3, 'rt')
data3.append('\"links\":[')
for line in edgefopen:
    source=line.split('\t')[0].strip()
    target=line.split('\t')[1].strip()
    Edge = Edge + 1
    if Edge <= (edgeNum - 1):
        newLine='{'+'\n'+'\"source\":'+source+',\n'+'\"target\":'+target+'\n'+'},'
    else:
        newLine='{'+'\n'+'\"source\":'+source+',\n'+'\"target\":'+target+'\n'+'}'
    data3.append(newLine)
data3.append(']')
data3.append('}')
edgefopen.close()

fopen = open(newFileName4,"w")
for line in data3:
    fopen.write(line)
    fopen.write('\n')
fopen.close()
print ('---TASK IS OVER---')