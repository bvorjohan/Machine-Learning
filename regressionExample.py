import pandas as pd
import quandl
import math
import scipy
import numpy as np
from scikit import preprocessing, cross_validation

'''

NON-FUNCTIONAL CODE. CHECK USING PYTHON 2.7

try:
  eval("1 if True else 2")
except SyntaxError:
  # doesn't have ternary

'''

df = quandl.get("WIKI/GOOGL")
# print(df.head())
df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
df["HL_PCT"] = (df["Adj. High"] - df["Adj. Close"]) / df["Adj. Close"] * 100
df["PCT_change"] = (df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"] * 100

df = df[["Adj. Close","HL_PCT","PCT_change","Adj. Volume"]]

# print(df.head())

forecast_col = "Adj. Close"
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.1*len(df)))

df["label"] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.tail())

X = np.array(df.drop(["label"],1))
y = np.array(df["label"])

X = preprocessing.scale(X)
X = X[:-forecast_out+1]

print(len(X), len(y))
