import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest,chi2,RFE
from pandas import read_excel
import sklearn.linear_model as lm

df = pd.read_csv('input.txt', header=None, delimiter = ",")
df = df.drop(columns=[0,1])
array=df.values
df1 = pd.DataFrame()
for i in range(0,10):
    x=np.delete(array[:,0:10], i, 1)
    y=array[:,i]
    model = lm.LinearRegression()
    model.fit(x,y)
    y_n=model.predict(x)
    df1[i]=y_n

df2 = pd.read_csv('input.txt', header=None, delimiter=",")
df2 = df2.drop(columns=[0,1,4,5,6,7,8,10,11])
array = df2.values
df3 = pd.DataFrame()
for i in range(0,3):
    x=np.delete(array[:,0:10], i, 1)
    y=array[:,i]
    model = lm.LinearRegression()
    model.fit(x,y)
    y_n=model.predict(x)
    df3[i]=y_n

l1 = list()
l2 = list()
l3 = list()
array=df1.values

i=0
while i < len(array):
    l1.append(((5 * array[i][0]) + ( 2 * array[i][3]) + (3 * array[i][6]) ) / 10)
    l2.append(((4 * array[i][1]) + (3 * array[i][9]) + (3 * array[i][7]) ) / 10)
    l3.append(((2 * array[i][8]) + (2 * array[i][2]) + (3 * (1-array[i][5])) + (3 * (1-array[i][5])) ) / 10)
    i+=1

df1[10] = l1
df1[11] = l2
df1[12] = l3

l1 = list()
l2 = list()
array=df3.values
i=0
while i < len(array):
    l1.append(((5 * array[i][0])) / 10)
    l2.append(((4 * array[i][1]) + (3 * array[i][2]) ) / 10)
    i+=1

df3[10] = l1
df3[11] = l2

np.savetxt(r'df1.txt', df1.values, fmt='%f')
np.savetxt(r'df3.txt', df3.values, fmt='%f')

#print(df1)
#print(df3)