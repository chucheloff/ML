import math
import random
import datetime
f = open("2.31 cleared.txt",'r',encoding='UTF-8')
lines = f.readlines()
f.close()
l = list()

for line in lines:
    arr = line.split(',')
    for i in range(2,12):
        arr[i] = (float)(arr[i])
    l.append(arr)

i=0
while i < len(l):
    l[i].append( ( (5 * l[i][1+1]) + ( 2 * l[i][4 + 1]) + (3 * l[i][7+1]) ) / 10 )
    #print(l[i][len(l[i])-1])

    l[i].append( ( (4 * l[i][2+1]) + (3 * l[i][10+1]) + (3 * l[i][8+1]) ) / 10)
    #print(l[i][len(l[i])-1])

    l[i].append( ( (2 * l[i][9+1]) + (2 * l[i][3+1]) + (3 * (1-l[i][6+1])) + (3 * (1-l[i][5+1])) ) / 10 )
   #print(l[i][len(l[i])-1])
    i+=1

f = open('31. generated.txt', 'w', encoding='UTF-8')
line = ''
for each in l:
    line = str(each[0])
    each.pop(0)
    for el in each:
        line += ',' + str(el)
    f.write(line+'\n')
f.close

