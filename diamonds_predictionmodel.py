import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plot
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def diamond_prediction(statistics):
    diamonds = pd.read_csv('diamonds.csv')

    diamonds.drop(diamonds.filter(regex='Unnamed'), axis = 1, inplace = True)

    diamonds.drop(['cut'],axis=1,inplace=True)
    diamonds.drop(['color'],axis=1,inplace=True)
    diamonds.drop(['clarity'],axis=1,inplace=True)
    
    
    x_train, x_test, y_train, y_test = train_test_split(diamonds.drop(['price'],axis=1),diamonds['price'],test_size=0.3,random_state = 42)
    
   
    model = RandomForestRegressor(random_state=42)
    model.fit(x_train,y_train)
    rezultat = x_test.copy()
    
    rezultat['carat'] = statistics[0]
    rezultat['depth'] = statistics[1]
    rezultat['table'] = statistics[2]
    rezultat['x'] = statistics[3]
    rezultat['y'] = statistics[4]
    rezultat['z'] = statistics[5]
    my_price = model.predict(rezultat)

    return my_price[1]

