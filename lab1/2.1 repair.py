import math
import random
import datetime
f = open("1. output.txt",'r',encoding='UTF-8')
lines = f.readlines()
f.close()
l = list()

for line in lines:
    arr = line.split(',')
    for i in range(2,12):
        arr[i] = (int)(arr[i])
    l.append(arr)

print(l)

i=0

while i < len(l):
    for k in range(2,12):
        sum_by_coef = 0
        coef_count = 0.0
        for j in range(0,5):
            if l[i+j][k] !=0:
                sum_by_coef += l[i+j][k]
                coef_count += 1.0
        for j in range(0,5):
            if l[i+j][k] == 0:
                coef = sum_by_coef / coef_count
                if (math.ceil(coef) - coef) > 0.5:
                    l[i+j][k] = math.ceil(coef) - 1 + random.randint(0,2)
                else:
                    l[i+j][k] = math.floor(coef) - 1 + random.randint(0,2)
                #safety
                if l[i+j][k] > 10:
                    l[i+j][k] = 10
                if l[i+j][k] <1:
                    l[i+j][k] = 1
    i+=5

for each in l:
    print((str)(each))

f = open('2.1 repaired.txt', 'w', encoding='UTF-8')
line = ''
for each in l:
    line = str(each[0])
    each.pop(0)
    for el in each:
        line += ',' + str(el)
    f.write(line+'\n')
f.close

