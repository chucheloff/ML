import datetime
from operator import itemgetter


start_date = datetime.datetime(2021,3,21)
f = open("0. input.txt",'r')
lines = f.readlines()
f.close()
l = list()


lines = lines[1:]
for line in lines:
    arr = line.split(';')
    d = arr[0].split('.')
    arr[0] = datetime.datetime(int(d[2]),int(d[1]),(int)(d[0]))
    for i in range(2,12):
        arr[i] = (int)(arr[i])
    l.append(arr)

l.sort(key=itemgetter(1))


f = open('1. output.txt','w')

c = 1
for i in range(0,len(l)):
    if l[i][1] == l[i+1][1]:
        c+=1
        if c > 5:
            l.pop(i+1)
            c-=1
            i-=1
    else:
        if c<5:
            for j in range(c,5):
                arr = list(l[i])
                for b in range(2,len(arr)):
                    arr[b] = 0
                l.append(arr)
        c=1

l.sort(key=itemgetter(1))

i = 0
while i < len(l)-4:
    for j in range(0,5):
        l[i][0] = start_date + datetime.timedelta(days = j*7)
        print((str)(l[i]))
        i+=1

line = ''
for each in l:
    line = str(each[0].date())
    each.pop(0)
    for el in each:
        line += ',' + str(el)
    f.write(line+'\n')
f.close
