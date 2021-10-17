from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.svm import SVC 
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from matplotlib import pyplot as plt
import pandas as p



df = p.read_csv('input.txt', header=None, delimiter = ",")

df1 = p.read_csv('df1.txt', header=None, delimiter = " ")
array = df.values
array1 = df1.values

x=array[:,2:11]
y=array[:,11]


x1=array1[:,0:12]
y1=array1[:,12]


test_size = 0.2
seed = 10
scoring = 'accuracy'
n_estimators = 100
num_folds = 10
x_train, x_test, y_train, y_test = train(x, y, test_size=test_size, random_state=seed)
x_train1, x_test1, y_train1, y_test1 = train(x1, y1, test_size=test_size, random_state=seed)
models = []
models.append(('LR', LogisticRegression()))
models.append(('SVC', SVC()))
models.append(('BG', BaggingClassifier(n_estimators=n_estimators)))
scores = []
names =[]
results = []
predictions = []
msg_row = []

a = "Полный датасет"
print (a)
for name, model in models:
    kfold = KFold(n_splits=num_folds)
    cv_results = cross_val_score(model, x_train, y_train, cv=kfold, scoring=scoring)
    names.append(name)
    results.append(cv_results)
    m_fit = model.fit(x_train, y_train)
    m_predict = model.predict(x_test)
    m_predict1 = model.predict(x_test1)
    predictions.append(m_predict)
    predictions.append(m_predict1)
    m_score = model.score(x_test, y_test)
    m_score1 = model.score(x_test1, y_test1)
    scores.append(m_score)
    scores.append(m_score1)
    msg = "%s: train = %.3f (%.3f) / test = %.3f (реал)" % (name, cv_results.mean(), cv_results.std(), m_score)
    msg1 = "%s: train = %.3f (%.3f) / test = %.3f (синтез)" % (name, cv_results.mean(), cv_results.std(), m_score1)
    msg_row.append(msg)
    msg_row.append(msg1)
    plt.plot([0, m_score], color = "yellow")
    plt.plot([0, m_score1], color = "green")
    print (msg)
    print (msg1)
    plt.show()

d = "Датасет с информатинвыми признаками"
print (d)
df2 = pd.read_excel(io='C:/Users/User/Desktop/Учёба/CS/3 лр/База(inf).xlsx', engine='openpyxl',usecols='A:J')
df3 = pd.read_excel(io='C:/Users/User/Desktop/Учёба/CS/3 лр/База(inf new).xlsx', engine='openpyxl',usecols='A:J')
array2 = df2.values
array3 = df3.values

x2=array2[:,0:7]
y2=array2[:,9]
x3=array3[:,0:7]
y3=array3[:,9]

x_train2, x_test2, y_train2, y_test2 = train(x2, y2, test_size=test_size, random_state=seed)
x_train3, x_test3, y_train3, y_test3 = train(x3, y3, test_size=test_size, random_state=seed)

for name, model in models:
    kfold = KFold(n_splits=num_folds)
    cv_results = cross_val_score(model, x_train2, y_train2, cv=kfold, scoring=scoring)
    names.append(name)
    results.append(cv_results)
    m_fit = model.fit(x_train2, y_train2)
    m_predict2 = model.predict(x_test2)
    m_predict3 = model.predict(x_test3)
    predictions.append(m_predict2)
    predictions.append(m_predict3)
    m_score2 = model.score(x_test2, y_test2)
    m_score3 = model.score(x_test3, y_test3)
    scores.append(m_score2)
    scores.append(m_score3)
    msg2 = "%s: train = %.3f (%.3f) / test = %.3f (реал)" % (name, cv_results.mean(), cv_results.std(), m_score2)
    msg3 = "%s: train = %.3f (%.3f) / test = %.3f (синтез)" % (name, cv_results.mean(), cv_results.std(), m_score3)
    msg_row.append(msg2)
    msg_row.append(msg3)
    plt.plot([0, m_score2], color = "blue")
    plt.plot([0, m_score3], color = "red")
    print (msg2)
    print (msg3)
    plt.show()

c = "Датасет с информатинвыми признаками только 1 класса"
print (c)
rslt_df =df2[df['инф'] == 1]
rslt_df1 =df3[df['инф'] == 1]
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df4 = rslt_df
df5 = rslt_df1

array4 = df4.values
array5 = df5.values

x4=array4[:,0:7]
y4=array4[:,9]
x5=array5[:,0:7]
y5=array5[:,9]

x_train4, x_test4, y_train4, y_test4 = train(x4, y4, test_size=test_size, random_state=seed)
x_train5, x_test5, y_train5, y_test5 = train(x5, y5, test_size=test_size, random_state=seed)

for name, model in models:
    kfold = KFold(n_splits=num_folds)
    cv_results = cross_val_score(model, x_train4, y_train4, cv=kfold, scoring=scoring)
    names.append(name)
    results.append(cv_results)
    m_fit = model.fit(x_train4, y_train4)
    m_predict4 = model.predict(x_test4)
    m_predict5 = model.predict(x_test5)
    predictions.append(m_predict4)
    predictions.append(m_predict5)
    m_score4 = model.score(x_test4, y_test4)
    m_score5 = model.score(x_test5, y_test5)
    scores.append(m_score4)
    scores.append(m_score5)
    msg4 = "%s: train = %.3f (%.3f) / test = %.3f (реал)" % (name, cv_results.mean(), cv_results.std(), m_score4)
    msg5 = "%s: train = %.3f (%.3f) / test = %.3f (синтез)" % (name, cv_results.mean(), cv_results.std(), m_score5)
    msg_row.append(msg4)
    msg_row.append(msg5)
    plt.plot([0, m_score4], color = "pink")
    plt.plot([0, m_score5], color = "black")
    print (msg4)
    print (msg5)
    plt.show()

