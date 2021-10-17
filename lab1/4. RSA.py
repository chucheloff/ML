#imports
import random

#constants
big_loops = 300

repeats = 20

n_range = 100

h = 100.0

grades = {
    1:[0.6,0.4],
    2:[0.5,0.3],
    3:[0.8,0.3],
    4:[0.6, 0.5],
    5:[0.7,0.3],
    6:[0.6,0.4],
    7:[0.7,0.4],
    8:[0.5, 0.25],
    9:[0.7, 0.45],
    10:[0.85, 0.35],
    11:[0.6,0.4],
    12:[0.8,0.4],
    13:[0.75,0.4]
}

def isGood(i,val):
    i+=1
    #return grade of value in [i] coeff 
    if val > grades[i][0]:
        return 1
    if val > grades[i][1]:
        return 0
    return -1


f = open("31. generated.txt",'r',encoding='UTF-8')
lines = f.readlines()
f.close()
l = list()

for line in lines:
    arr = line.split(',')
    for i in range(2,15):
        arr[i] = (float)(arr[i])
    l.append(arr)

g = [0 for i in range(0,13)]

#g[k] == l[i][k+2]
for i in range(0,13):
    g[i] = 1/13

for big_loop in range(0,big_loops):
    n_max = []
    n_min = []
    grade_max = 0
    grade_min = 1000000
    coef = 0
    for r in range(0,repeats):
        proxy = []
        grade = 0
        for n in range(0,n_range):
            el = random.uniform(0,1)
            s = 0
            for i in range(0,13):
                if i == 0 and el < g[i]:
                    rand = random.randint(0,len(l)-1)
                    val = l[rand][i+2]
                    #exception for question 5
                    coef = i
                    if i == 5 or i == 6:
                        val = 1 - val
                    grade += isGood(i,val)
                else:
                    if el > s and el < (s + g[i]):
                        #rand = random element from input 
                        rand = random.randint(0,len(l)-1)
                        val = l[rand][i+2]
                        #exception for question 5 and 6
                        coef = i
                        if i == 5 or i == 6:
                            val = 1 - val
                        grade += isGood(i,val)
                s += g[i]
            proxy.append(coef)
        if grade > grade_max:
            n_max = proxy
            grade_max = grade
        if grade < grade_min:
            n_min = proxy
            grade_min = grade


    count = [0 for i in range(0,len(g))]
    for ind in n_max:
        count[ind]+=1

    maxx = 0;
    for ind in range(0,len(count)):
        if count[ind] > count[maxx]:
            maxx = ind

    for ind in n_min:
        count[ind]+=1
    
    minn = 0
    for ind in range(0,len(count)):
        if count[ind] > count[minn]:
            minn = ind

    #поощрение
    for ind in range(0,len(g)):
        if ind != maxx:
            g[ind] -= (g[maxx] / h) / (float)(len(g)-1)
    g[maxx] += g[maxx]/h
    
    #наказание
    for ind in range(0,len(g)):
        if ind != minn:
            g[ind] += (g[minn] / h) / (float)(len(g)-1)
    g[minn] -= g[minn]/h


    #компенсация ошибки
    s = 0
    for each in g:
        s += each
    error = 0.0
    error = 1.0 - s
    part = 0.0
    part = error/len(g)
    for ind in range(0,len(g)):
        g[ind] += part

#answer
for each in g:
    print(each)
