import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


#Loading the data
data= pd.read_csv('winequality-red.csv')

##Null values
nulls = pd.DataFrame(data.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

#Finding correlation with the target class
numeric_features = data.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print (corr['quality'].sort_values(ascending=False)[1:4], '\n')

#Dropping the columns having less correlation with target class
data=data.drop(columns=['residual sugar','free sulfur dioxide','pH'],axis=1)
print(data.columns)

#Splitting data
X = data.drop('quality', axis=1)
y = data['quality']
X_train, X_test,y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=200)

#creation of regression model and training it
model=LinearRegression().fit(X_train,y_train)

#predicting the target
predict=model.predict(X_test)

#evaluation of model using metrics
MSE = mean_squared_error(y_test, predict)
r2_score = r2_score(y_test,predict)
print("Mean squared error :",MSE)
print("R2 score : ",r2_score)




