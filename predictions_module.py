import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import plotly.express as px
plt.style.use('bmh')
def predict_close(df,ahead):
    df = df[['Close']]
    predict_for = int(ahead)
    df['Predicted'] = df[['Close']].shift(-predict_for)
    x = np.array(df.drop(['Predicted'],1))[:-predict_for]
    y = np.array(df['Predicted'])[:-predict_for]
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.25)
    tree_model = DecisionTreeRegressor().fit(x_train,y_train)
    lr_model = LinearRegression().fit(x_train,y_train)
    x_predicted = df.drop(['Predicted'],1)[:-predict_for]
    x_predicted = x_predicted.tail(predict_for)
    x_predicted = np.array(x_predicted)
    tree_prediction_model = tree_model.predict(x_predicted)
    #print(tree_prediction_model)
    lr_prediction_model = lr_model.predict(x_predicted)
    #print(lr_prediction_model)
    predictions = tree_prediction_model
    valid = df[x.shape[0]:]
    valid['Predicted'] = predictions
    plt.figure(figsize=(30,9))
    plt.title('Predicted Closing price')
    plt.xlabel('Days')
    plt.ylabel('Close Price')
    plt.plot(df['Close'])
    plt.plot(valid[['Close', 'Predicted']])
    plt.legend(['original','valid','Predicted'])
    plt.show()
def predict_open(df,ahead):
    df = df[['Open']]
    predict_for = int(ahead)
    df['Predicted'] = df[['Open']].shift(-predict_for)
    x = np.array(df.drop(['Predicted'],1))[:-predict_for]
    y = np.array(df['Predicted'])[:-predict_for]
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.25)
    tree_model = DecisionTreeRegressor().fit(x_train,y_train)
    lr_model = LinearRegression().fit(x_train,y_train)
    x_predicted = df.drop(['Predicted'],1)[:-predict_for]
    x_predicted = x_predicted.tail(predict_for)
    x_predicted = np.array(x_predicted)
    tree_prediction_model = tree_model.predict(x_predicted)
    #print(tree_prediction_model)
    lr_prediction_model = lr_model.predict(x_predicted)
    #print(lr_prediction_model)
    predictions = tree_prediction_model
    valid = df[x.shape[0]:]
    valid['Predicted'] = predictions
    plt.figure(figsize=(40,15))
    plt.title('Predicted Opening price')
    plt.xlabel('Days')
    plt.ylabel('Open Price')
    plt.plot(df['Open'])
    plt.plot(valid[['Open', 'Predicted']])
    plt.legend(['original','valid','Predicted'])
    plt.show()
