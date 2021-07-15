import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.datasets import load_iris
import pickle


df_iris = load_iris()
df_iris.keys()

df = pd.DataFrame(df_iris.data, columns=[
                  'sepal length', 'sepal width', 'petal length', 'petal width'])

y = df_iris.target
X = df

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=1, test_size=0.2)


def train():
    for i in range(100, 500, 50):
        clf_r = RandomForestClassifier(n_estimators=i)
        clf_r = clf_r.fit(X_train, y_train)
        pred_r = clf_r.predict(X_test)
        acc = sum((y_test-pred_r) == 0) / len(pred_r)
    print(acc)
    return pred_r


model = train()

# save model
with open('./iris_model.pkl', 'wb') as file:
    pickle.dump(model, file)
