from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use("fivethirtyeight")


X = np.array([1,2,3,4,5,6], dtype=np.float64)
Y = np.array([5,4,6,5,6,7], dtype=np.float64)

# plt.scatter(X,Y)
# plt.show()

def create_dataset(size, variance, step = 2, correlation = False):
    val = 1
    Y = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        Y.apend(y)    
    return np.array(X, dtype=np.float64), np.array(Y, dtype=np.float64)


def best_fit_slope_intercept(X,Y):

    m = ( (mean(X)*mean(Y) - mean(X*Y)) /
        (mean(X)**2 - mean(X**2)))

    b = mean(Y) - m*mean(X)
    return m,b

def SE(Y_orig, Y_line):
    return sum((Y_line-Y_orig)**2)

def R_squared(Y_orig,Y_line):
    mean_line = [mean(Y_orig) for y in Y_orig]
    SE_regr = SE(Y_orig, Y_line)
    SE_mean = SE(Y_orig, mean_line)
    return 1-(SE_regr/SE_mean)

m,b = best_fit_slope_intercept(X,Y)

regression_line = [(m*x)+b for x in X]

predict_x = 8
predict_y = (m*predict_x)+b

R_squared = R_squared(Y, regression_line)
print(R_squared)

plt.scatter(X,Y)
plt.scatter(predict_x,predict_y,color="g")
plt.plot(X,regression_line)
plt.show()
