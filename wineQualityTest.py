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

#dividing data into training & testing
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=3)
regressor = LinearRegression()
regressor.fit(x_train,y_train)

#predicting
regressor.coef_
train_pred = regressor.predict(x_train)
train_pred
test_pred=regressor.predict(x_test)
test_pred

#predicted data
predicted_data = np.round_(test_pred)
predicted_data
coeffecients = pd.DataFrame(regressor.coef_,features)
coeffecients.columns = ['Coeffecient']
coeffecients

