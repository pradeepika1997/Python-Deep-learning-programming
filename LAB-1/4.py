import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


#loading data
bh_data = load_boston()
boston = pd.DataFrame(bh_data.data, columns=bh_data.feature_names)
print(boston.columns)
boston['MEDV'] = bh_data.target

### Displaying null value count
nulls = pd.DataFrame(boston.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

###Replacing null values with mean
boston = boston.select_dtypes(include=[np.number]).interpolate().dropna()

## Displaying Null value count after replacing with mean
nulls = pd.DataFrame(boston.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

###Finding correlation with target class
numeric_features = boston.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print (corr['MEDV'].sort_values(ascending=False)[1:4], '\n')


#Dropping the columns having less correlation with target class
boston=boston.drop(columns=['PTRATIO', 'TAX', 'RAD', 'DIS', 'AGE', 'NOX', 'CHAS', 'INDUS', 'CRIM'],axis=1)
print(boston.columns)

#Splitting data

X = boston.drop('MEDV', axis=1)
y = boston['MEDV']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=9)


#creation of regression model and training it
model=LinearRegression().fit(X_train,y_train)

#predicting the target
predict=model.predict(X_test)

#evaluation of model using metrics
MSE = mean_squared_error(y_test, predict)
r2_score = r2_score(y_test,predict)
print("Mean squared error :",MSE)
print("R2 score : ",r2_score)