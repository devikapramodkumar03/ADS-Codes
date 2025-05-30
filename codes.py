# -*- coding: utf-8 -*-
"""codes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_CC-kPfNEsaSeMHRhczhcnyoaBptlmFa
"""

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()

iris.feature_names

iris.target_names

df=pd.DataFrame(iris.data,columns=iris.feature_names)
df.head()

df['target']=iris.target
df.head()

df['flower_name']=df.target.apply(lambda x:iris.target_names[x])
df.head()

df0=df[:50]
df1=df[50:100]
df2=df[100:]

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

"""Sepal length vs Sepal width (sentosa vs versicolor)"""

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.scatter(df0['sepal length (cm)'],df0['sepal width (cm)'],color='green',marker='+')
plt.scatter(df1['sepal length (cm)'],df1['sepal width (cm)'],color='blue',marker='.')

"""Train using Support Vector Machine (SVM)"""

from sklearn.model_selection import train_test_split

x=df.drop(['target','flower_name'],axis='columns')
y=df.target

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

len(X_train)

len(X_test)

from sklearn.svm import SVC
model=SVC()

model.fit(X_train,y_train)

model.score(X_train,y_train)

"""1. Regularization"""

model_C=SVC(C=1)
model_C.fit(X_train,y_train)
model_C.score(X_train,y_train)

model_C=SVC(C=10)
model_C.fit(X_train,y_train)
model_C.score(X_train,y_train)

"""2. Gamma"""

model_g=SVC(gamma=10)
model_g.fit(X_train,y_train)
model_g.score(X_train,y_train)

"""3. Kernal"""

model_linear_kernal=SVC(kernel='linear')
model_linear_kernal.fit(X_train,y_train)

model_linear_kernal.score(X_test,y_test)