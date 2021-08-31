import numpy as np
import math
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from pprint import pprint

def distance(x,y):
    return int(math.floor(math.sqrt(x**2 + y**2)))

def feature_lift(x):
    return [x**4, x**3, x**2, x**1, x**0]

def normalize(x):
    return x/100

def txt_to_list(files):
    data = []
    for file in files:
        temp_file=open(file, 'r')
        content=temp_file.read()
        content_list=content.split('\n')
        content_list.pop(-1)
        xs = []
        ys = []
        for c in content_list:
            temp = eval(c)
            xs.append(feature_lift(normalize(distance(temp[0]/12, temp[1]/12))))
            ys.append(temp[2])
        data.append([xs,ys])
    return data

def list_to_fit(data):
    for i in range(len(data)):
        print("Fitting {}".format(files[i]))
        X_train, X_test, y_train, y_test = train_test_split(np.array(data[i][0]), np.array(data[i][1]), test_size = 0.20, random_state = 5)
        print(X_train.shape)
        print(X_test.shape)
        print(y_train.shape)
        print(y_test.shape)
        model = LogisticRegression(random_state=0, multi_class='multinomial', penalty='none', solver='newton-cg')
        model.fit(X_train, y_train)
        preds1 = model.predict(X_test)
        print("Accuracy Score: {}".format(metrics.accuracy_score(y_test, preds1)))
        X_test2 = np.array([feature_lift(normalize(x)) for x in range(0,51,5)])
        preds2 = model.predict(X_test2)
        pprint(list(zip([x for x in range(0,51,5)], preds2)))
        print()

files = ['Steph_Curry.txt','Chris_Paul.txt', 'Zion_Williamson.txt']
shot_data = txt_to_list(files)
list_to_fit(shot_data)
