# code contains about training of the model
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

df= pd.read_csv('housing.csv').iloc[:, :-1].dropna()

x=df.drop(columns=['Price'])
y=df['Price']

model= LinearRegression()
model.fit(x,y)
joblib.dump(model, 'model.joblib')
