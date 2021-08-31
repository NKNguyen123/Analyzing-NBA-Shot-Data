import numpy as np
import math
from sklearn.linear_model import LinearRegression
from pprint import pprint

def distance(x,y):
    return int(math.floor(math.sqrt(x**2 + y**2)))

files=['Steph_Curry.txt','Chris_Paul.txt', 'Zion_Williamson.txt']
xs=[]
ys=[]
for file in files:
    temp_file=open(file, 'r')
    content=temp_file.read()
    content_list=content.split('\n')
    content_list.pop(-1)
    temp_xs=[]
    temp_ys=[]
    for c in content_list:
        temp=eval(c)
        temp_xs.append(distance(temp[0]/12, temp[1]/12))
        temp_ys.append(temp[2])
    xs.append(temp_xs)
    ys.append(temp_ys)

model = LinearRegression()

for i in range(3):
    print("Fitting {}".format(files[i]))
    x = np.array(xs[i]).reshape(-1,1)
    y = np.array(ys[i])
    model.fit(x,y)
    r_sq = model.score(x,y)
    print("coefficient of determination: {}".format(r_sq))
    print("intercept: {}".format(model.intercept_))
    print("slope: {}".format(model.coef_))
    x_pred = [0,5,10,15,20,25,30,35,40,45,50]
    y_pred = model.predict(np.array(x_pred).reshape(-1,1))
    print("(Range (ft.), Predicted % Of Scoring):")
    pprint(list(zip(x_pred,y_pred)))
    print()
