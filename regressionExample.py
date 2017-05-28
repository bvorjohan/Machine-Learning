import pandas as pd
import quandl, math, datetime, time
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style


'''
reference https://www.youtube.com/watch?v=QLVMqwpOLPk&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=5
'''

style.use("ggplot")

# getting data
df = quandl.get("WIKI/GOOGL")

# filtering out unwanted data
df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]

# calculating differential gain
df["HL_PCT"] = (df["Adj. High"] - df["Adj. Close"]) / df["Adj. Close"] * 100

# calculatiung percent gain
df["PCT_change"] = (df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"] * 100

# filtering out data that was used to calculate new data
df = df[["Adj. Close","HL_PCT","PCT_change","Adj. Volume"]]


# declaration of data to be forecasted
forecast_col = "Adj. Close"
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
# print(forecast_out)

df["label"] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(["label"],1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)
y = np.array(df["label"])

# X = X[:-forecast_out+1]

# print(len(X), len(y))


X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)

clf = LinearRegression()
# clf = svm.SVR()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test,y_test)

# print(accuracy)

forecast_set = clf.predict(X_lately)

print(forecast_set,accuracy,forecast_out)

df["Forecast"] = np.nan

last_date = df.iloc[-1].name
last_unix = time.mktime(last_date.timetuple())
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

print(df.head)

df["Adj. Close"].plot()

df["Forecast"].plot()
plt.legend(loc=4)
plt.show()
