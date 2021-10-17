f = open("2.21 normalized.txt",'r',encoding='UTF-8')
lines = f.readlines()
f.close()
l = list()

for line in lines:
    arr = line.split(',')
    for i in range(2,12):
        arr[i] = (float)(arr[i])
    l.append(arr)

def check(el,g):
    for j in range(0,len(g)):
        flag1 = True
        for k in range(2,12):
            if el[k] != g[j][k]:
                flag1 = False
        if flag1 and el[1] == g[j][1] :
            return False
    return True
g = []
g.append(l[0])
for i in range(1,len(l)):
    if check(l[i],g):
        g.append(l[i])

print(g)
f = open('2.31 cleared.txt', 'w', encoding='UTF-8')
line = ''
for each in g:
    line = str(each[0])
    each.pop(0)
    for el in each:
        line += ',' + str(el)
    f.write(line+'\n')
f.close()