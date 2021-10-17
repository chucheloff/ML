import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.datasets as ds
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest,chi2,RFE
from pandas import read_excel
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import datasets
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn import model_selection

print('--РЕАЛЬНЫЙ Dataset--')
df = pd.read_csv('input.txt', header=None, delimiter = ",")
array = df.values
X = df.iloc[:, 2:11].values
y = df.iloc[:,11].values.reshape((-1,1))

X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.2,random_state=10)
print(X_train.shape, X_test.shape)


print('--СИНТЕЗИРОВАННЫЙ Dataset--')
df2 = pd.read_csv('df1.txt', header=None, delimiter = " ")
X2 = df2.iloc[:, 0:9].values
y2 = df2.iloc[:, 9].values.reshape((-1,1))

X2_train,X2_test,y2_train,y2_test=train_test_split(X2,y2,train_size=0.2,random_state=10)

print(X2_train.shape, X2_test.shape)


print('--Метод случайный лес--')
model = rfc()
model.fit(X_train, y_train)
#RandomForestClassifier()
exit()
xs1=model.score(X_test, y_test)
print(xs1)
xs2=model.score(X2_test, y2_test)
print(xs2)


exit()


print('--Метод ближайших соседей--')
model2= KNeighborsClassifier()
model2.fit(X_train, y_train)
KNeighborsClassifier()
xs4=model2.score(X2_test, y2_test)
xs3=model2.score(X_test, y_test)
print(xs3)

print(xs4)


print('--Метод наивный байес--')
model3= MultinomialNB()
model3.fit(X_train, y_train)
MultinomialNB()
xs5=model3.score(X_test, y_test)
xs6=model3.score(X2_test, y2_test)
print(xs5)

print(xs6)


print('--График по первому методу--')
plt.plot([0, xs1])
plt.plot([0, xs2])
plt.show()

print('--График по второму методу--')
plt.plot([0, xs3])
plt.plot([0, xs4])
plt.show()

print('--График по третьему методу--')
plt.plot([0, xs5])
plt.plot([0, xs6])
plt.show()

print('--Отображение методов на одном графике--')
plt.plot([0, xs1], color = "blue")
plt.plot([0, xs2], color = "blue")
plt.plot([0, xs3], color = "red")
plt.plot([0, xs4], color = "red")
plt.plot([0, xs5], color = "green")
plt.plot([0, xs6], color = "green")
plt.show()

print('--Разница между ошибками оказалась большая. Проведем еще один эксперимент, взяв за X лучшие 3 значения(столбцы)--')
X = df.iloc[:, 10:12].values
y = df.iloc[:, 13].values

X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.2,random_state=10)

X2 = df2.iloc[:, 9:11].values
y2 = df2.iloc[:, 12].values

X2_train,X2_test,y2_train,y2_test=train_test_split(X2,y2,train_size=0.2,random_state=10)

model.fit(X_train, y_train)
RandomForestClassifier()
xs1=model.score(X_test, y_test)
xs2=model.score(X2_test, y2_test)
print(xs1)

print(xs2)


model2= KNeighborsClassifier()
model2.fit(X_train, y_train)
KNeighborsClassifier()
xs3=model2.score(X_test, y_test)
xs4=model2.score(X2_test, y2_test)
print(xs3)

print(xs4)


model3= MultinomialNB()
model3.fit(X_train, y_train)
MultinomialNB()
xs5=model3.score(X_test, y_test)
xs6=model3.score(X2_test, y2_test)
print(xs5)
print(xs6)

print('--Проведем еще один эксперимент, исключив 3 наихудших значения(столбца)--')
df = pd.read_excel(io=r'C:\универ\Специальные главы CS\ЛР5готов\Почтиконец2.xlsx', engine='openpyxl', usecols='B:M')
df2 = pd.read_excel(io=r'C:\универ\Специальные главы CS\ЛР5готов\ПунктКонОкругСрЗначПризнакКласс2.xlsx', engine='openpyxl', usecols='B:L')

X = df.iloc[:, 3:9].values
y = df.iloc[:, 10].values

X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.2,random_state=10)

X2 = df2.iloc[:, 2:8].values
y2 = df2.iloc[:, 9].values

X2_train,X2_test,y2_train,y2_test=train_test_split(X2,y2,train_size=0.2,random_state=10)

model = RandomForestClassifier()
model.fit(X_train, y_train)
RandomForestClassifier()
xs2=model.score(X2_test, y2_test)
xs1=model.score(X_test, y_test)
print(xs1)
print(xs2)

model2= KNeighborsClassifier()
model2.fit(X_train, y_train)
KNeighborsClassifier()
xs3=model2.score(X_test, y_test)
xs4=model2.score(X2_test, y2_test)
print(xs3)
print(xs4)

model3= MultinomialNB()
model3.fit(X_train, y_train)
MultinomialNB()
xs5=model3.score(X_test, y_test)
xs6=model3.score(X2_test, y2_test)
print(xs5)
print(xs6)