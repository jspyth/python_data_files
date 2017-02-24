# coding=utf-8
# 去除数据文件里的重复行
fin = open("final.txt",'r')
fout = open('output.txt','w')
bufferedlines = []
num = 0
bufferedlines = fin.readlines()
bufferedlines.sort()
result = list(set(bufferedlines))
result.sort()
for line in result:
    print(line)
    fout.write(line)