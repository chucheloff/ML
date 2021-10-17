from matplotlib import pyplot as plt
import pandas as p

filename = 'input.txt'

df = pd.read_csv(filename, header=None, delimiter = ",")
df = df.drop(columns=[0,1])
array=df.values
for i in range(0,10):
    x=array[:,i for i in range(0,10)]
    y=array[:,i]
    model = lm.LinearRegression()

