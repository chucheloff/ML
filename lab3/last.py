import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.datasets as ds
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.feature_selection import SelectKBest,chi2,RFE
from sklearn.ensemble import ExtraTreesRegressor
from sklearn import datasets
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn import model_selection

print('--РЕАЛЬНЫЙ Dataset--')
df = pd.read_csv('input.txt', header=None, delimiter = ",")
array = df.values
X = df.iloc[:, 2:11].values
y = df.iloc[:,11].values

X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.2,random_state=10)
print(X_train.shape, X_test.shape)


print('--СИНТЕЗИРОВАННЫЙ Dataset--')
df2 = pd.read_csv('df1.txt', header=None, delimiter = " ")
X2 = df2.iloc[:, 0:9].values
y2 = df2.iloc[:, 9].values

X2_train,X2_test,y2_train,y2_test=train_test_split(X2,y2,train_size=0.2,random_state=10)

print(X2_train.shape, X2_test.shape)


print('--Метод случайный лес--')
model = RandomForestRegressor()
model.fit(X_train, y_train)
RandomForestRegressor()
xs1=model.score(X_test, y_test)
print(xs1)
xs2=model.score(X2_test, y2_test)
print(xs2)
print(model.get_params())


print('--Метод ближайших соседей--')
model2= KNeighborsRegressor()
model2.fit(X_train, y_train)
KNeighborsRegressor()
xs4=model2.score(X2_test, y2_test)
xs3=model2.score(X_test, y_test)
print(xs3)
print(xs4)
print(model2.get_params())


print('--Метод экстра деревья--')
model3 = ExtraTreesRegressor()
model3.fit(X_train, y_train)
ExtraTreesRegressor()
xs5=model3.score(X_test, y_test)
print(xs5)
xs6=model3.score(X2_test, y2_test)
print(xs6)
print(model3.get_params())

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

