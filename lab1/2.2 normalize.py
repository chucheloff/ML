import math
import random
import datetime
f = open("2.1 repaired.txt",'r',encoding='UTF-8')
lines = f.readlines()
f.close()
l = list()

for line in lines:
    arr = line.split(',')
    for i in range(2,12):
        arr[i] = (int)(arr[i])
    l.append(arr)

for k in range(2,12):
    maxx = l[0][k]
    minn = l[0][k]
    for j in range(1,len(l)):
        if l[j][k] < minn :
            minn = l[j][k]
        if l[j][k] > maxx:
            maxx = l[j][k] 
    for j in range(0,len(l)):
        if minn != 1:
            print(minn)
        if maxx != 10:
            print(maxx)
        if minn==maxx:
            maxx+=1
        l[j][k] = (l[j][k] - minn) / (maxx - minn)
i+=5

f = open('2.2 normalized.txt', 'w', encoding='UTF-8')
line = ''
for each in l:
    line = str(each[0])
    each.pop(0)
    for el in each:
        line += ',' + str(el)
    f.write(line+'\n')
f.close