import pandas
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris=datasets.load_iris()

features=iris.data
label=iris.target
# print(iris.DESCR)

df=KNeighborsClassifier()
df.fit(features, label)
print("enter the sepal length ")
a=input()
print("enter the sepal width ")
b=input()
print("enter the petal length ")
c=input()
print("enter the petal width ")
d=input()
r=[a,b,c,d]

go=df.predict([r])
if go==0:
    print("It is Setosa")
elif go==1:
    print("It is Versicolor")
elif go==2:
    print("It is Verginica")
print(go)


