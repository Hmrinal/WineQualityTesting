#importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#importing file
df= pd.read_csv('winequality-red.csv')
df.describe()
correlations = df.corr()['quality'].drop('quality')
print(correlations)

#visualizing through heatmap
sns.heatmap(df.corr())
plt.show()

#creating function features
def get_features(correlation_threshold):
    abs_corrs = correlations.abs()
    high_correlations = abs_corrs[abs_corrs > correlation_threshold].index.values.tolist()
    return high_correlations

#allocating X & Y values
features = get_features(0.05)
print(features)
x = df[features]
y = df['quality']