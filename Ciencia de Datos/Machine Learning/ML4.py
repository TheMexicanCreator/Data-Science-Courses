Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> from sklearn.metrics import r2_score, mean_squared_error
>>> from math import sqrt

>>> import os
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> data= pd.read_csv('advertising.csv', index_col=0)
>>> data.head()
       Radio  Newspaper  Sales
TV                            
230.1   37.8       69.2   22.1
44.5    39.3       45.1   10.4
17.2    45.9       69.3    9.3
151.5   41.3       58.5   18.5
180.8   10.8       58.4   12.9
>>> data.columns= ['TV','Radio','Newspaper','Sales']
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    data.columns= ['TV','Radio','Newspaper','Sales']
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 5596, in __setattr__
    return object.__setattr__(self, name, value)
  File "pandas/_libs/properties.pyx", line 70, in pandas._libs.properties.AxisProperty.__set__
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 769, in _set_axis
    self._mgr.set_axis(axis, labels)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/internals/managers.py", line 214, in set_axis
    self._validate_set_axis(axis, new_labels)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/internals/base.py", line 64, in _validate_set_axis
    raise ValueError(
ValueError: Length mismatch: Expected axis has 3 elements, new values have 4 elements
>>> data= pd.read_csv('advertising.csv', index_col=0)
>>> data= pd.read_csv('advertising.csv')
>>> data.head()
      TV  Radio  Newspaper  Sales
0  230.1   37.8       69.2   22.1
1   44.5   39.3       45.1   10.4
2   17.2   45.9       69.3    9.3
3  151.5   41.3       58.5   18.5
4  180.8   10.8       58.4   12.9
>>> data.columns= ['TV','Radio','Newspaper','Sales']
>>> data.shape
(200, 4)
>>> fig,axes= plt.subplots(1,3,sharey=True)
>>> data.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(16,8))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(16,8))
NameError: name 'axs' is not defined
>>> data.plot(kind='scatter',x='TV',y='Sales',ax=axes[0],figsize=(16,8))
<AxesSubplot:xlabel='TV', ylabel='Sales'>
>>> data.plot(kind='scatter',x='TV',y='Sales',ax=axes[1])
<AxesSubplot:xlabel='TV', ylabel='Sales'>
>>> data.plot(kind='scatter',x='Radio',y='Sales',ax=axes[1])
<AxesSubplot:xlabel='Radio', ylabel='Sales'>
>>> data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axes[2])
<AxesSubplot:xlabel='Newspaper', ylabel='Sales'>
>>> plt.show()
>>> feature_cols= ['TV']
>>> x= data[feature_cols]
>>> y= data.sales
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    y= data.sales
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 5583, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'sales'
>>> y= data.Sales
>>> from sklearn.linear_model import LinearRegression
>>> lm= LinearRegression
>>> lm.fit(x,y)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    lm.fit(x,y)
TypeError: fit() missing 1 required positional argument: 'y'
>>> lm= LinearRegression()
>>> lm.fit(x,y)
LinearRegression()
>>> print(lm.intercept_)
7.032593549127695
>>> print(lm.coef_)
[0.04753664]
>>> 7.032593549127695+[0.04753664]*50
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    7.032593549127695+[0.04753664]*50
TypeError: unsupported operand type(s) for +: 'float' and 'list'
>>> 7.032593549127695+0.04753664*50
9.409425549127695
>>> X_new= pd.DataFrame({'TV':[50]})
>>> X_new.head()
   TV
0  50
>>> lm.predict(X_new)
array([9.40942557])
>>> X_new= pd.DataFrame({'TV': [data.TV.min(),data.TV.max()]})
>>> X_new.head()
      TV
0    0.7
1  296.4
>>> preds= lm.predict(X_new)
>>> preds
array([ 7.0658692 , 21.12245377])
>>> data.plot(kind='scatter',x='TV',y='Sales')
<AxesSubplot:xlabel='TV', ylabel='Sales'>
>>> plt.plot(X_new,preds,c='red',linewidth)
SyntaxError: positional argument follows keyword argument
>>> plt.plot(X_new,preds,c='red',linewidth=2)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3621, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 136, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 142, in pandas._libs.index.IndexEngine.get_loc
TypeError: '(slice(None, None, None), None)' is an invalid key

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    plt.plot(X_new,preds,c='red',linewidth=2)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/pyplot.py", line 2757, in plot
    return gca().plot(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/axes/_axes.py", line 1632, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/axes/_base.py", line 312, in __call__
    yield from self._plot_args(this, kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/axes/_base.py", line 487, in _plot_args
    x = _check_1d(xy[0])
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/cbook/__init__.py", line 1327, in _check_1d
    ndim = x[:, None].ndim
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/frame.py", line 3506, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3628, in get_loc
    self._check_indexing_error(key)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5637, in _check_indexing_error
    raise InvalidIndexError(key)
pandas.errors.InvalidIndexError: (slice(None, None, None), None)
>>> plt.plot(X_new,preds,c='red')
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3621, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 136, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 142, in pandas._libs.index.IndexEngine.get_loc
TypeError: '(slice(None, None, None), None)' is an invalid key

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    plt.plot(X_new,preds,c='red')
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/pyplot.py", line 2757, in plot
    return gca().plot(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/axes/_axes.py", line 1632, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/axes/_base.py", line 312, in __call__
    yield from self._plot_args(this, kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/axes/_base.py", line 487, in _plot_args
    x = _check_1d(xy[0])
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/cbook/__init__.py", line 1327, in _check_1d
    ndim = x[:, None].ndim
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/frame.py", line 3506, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3628, in get_loc
    self._check_indexing_error(key)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5637, in _check_indexing_error
    raise InvalidIndexError(key)
pandas.errors.InvalidIndexError: (slice(None, None, None), None)
>>> plt.plot(X_new,preds,c='red',linewidth=2)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3621, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 136, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 142, in pandas._libs.index.IndexEngine.get_loc
TypeError: '(slice(None, None, None), None)' is an invalid key

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    plt.plot(X_new,preds,c='red',linewidth=2)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/pyplot.py", line 2757, in plot
    return gca().plot(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/axes/_axes.py", line 1632, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/axes/_base.py", line 312, in __call__
    yield from self._plot_args(this, kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/axes/_base.py", line 487, in _plot_args
    x = _check_1d(xy[0])
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/cbook/__init__.py", line 1327, in _check_1d
    ndim = x[:, None].ndim
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/frame.py", line 3506, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3628, in get_loc
    self._check_indexing_error(key)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5637, in _check_indexing_error
    raise InvalidIndexError(key)
pandas.errors.InvalidIndexError: (slice(None, None, None), None)
>>> plt.show()
>>> import statsmodels.formula.api as smf
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    import statsmodels.formula.api as smf
ModuleNotFoundError: No module named 'statsmodels'
>>> import statsmodels.formula.api as smf

Warning (from warnings module):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/statsmodels/compat/pandas.py", line 65
    from pandas import Int64Index as NumericIndex
FutureWarning: pandas.Int64Index is deprecated and will be removed from pandas in a future version. Use pandas.Index with the appropriate dtype instead.
>>> lm= smf.ols(formula='Sales ~ TV', data=data).fit()
>>> lm.conf_int()
                  0         1
Intercept  6.129719  7.935468
TV         0.042231  0.052843
>>> lm.pvalues
Intercept    1.406300e-35
TV           1.467390e-42
dtype: float64
>>> lm.rsquared
0.611875050850071
>>> feature_cols= ['TV','Radio','Newspaper']
>>> X= data[feature_cols]
>>> y= data.Sales
>>> from sklearn import model_selection
>>> xtrain,xtest,ytrain,ytest= model_selection.train_test_split(X,y,test_size=0.3, random_state=42)
>>> lm= LinearRegression()
>>> lm.fit(X,y)
LinearRegression()
>>> print(lm.intercept_)
2.938889369459412
>>> print(lm.coef_)
[ 0.04576465  0.18853002 -0.00103749]
>>> lm= LinearRegression()
>>> lm.fit(xtrain,ytrain)
LinearRegression()
>>> print(lm.intercept_)
2.7089490925159048
>>> print(l.coef_)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(l.coef_)
NameError: name 'l' is not defined
>>> print(lm.coef_)
[0.04405928 0.1992875  0.00688245]
>>> predictions= lm.predict(xtest)
>>> print(sqrt(mean_squared_error(ytest,predictions)))
1.9485372043446385
>>> lm= smf.ols(formula='Sales~TV + Radio + Newspaper'. data=data).fit()
SyntaxError: invalid syntax
>>> lm= smf.ols(formula='Sales~TV + Radio + Newspaper', data=data).fit()
>>> lm.conf_int()
                  0         1
Intercept  2.323762  3.554016
TV         0.043014  0.048516
Radio      0.171547  0.205513
Newspaper -0.012616  0.010541
>>> lm.summary()
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  Sales   R-squared:                       0.897
Model:                            OLS   Adj. R-squared:                  0.896
Method:                 Least Squares   F-statistic:                     570.3
Date:                Thu, 03 Feb 2022   Prob (F-statistic):           1.58e-96
Time:                        15:15:13   Log-Likelihood:                -386.18
No. Observations:                 200   AIC:                             780.4
Df Residuals:                     196   BIC:                             793.6
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      2.9389      0.312      9.422      0.000       2.324       3.554
TV             0.0458      0.001     32.809      0.000       0.043       0.049
Radio          0.1885      0.009     21.893      0.000       0.172       0.206
Newspaper     -0.0010      0.006     -0.177      0.860      -0.013       0.011
==============================================================================
Omnibus:                       60.414   Durbin-Watson:                   2.084
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              151.241
Skew:                          -1.327   Prob(JB):                     1.44e-33
Kurtosis:                       6.332   Cond. No.                         454.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""
>>> lm= smf.ols(formula='Sales~TV + Radio', data=data).fit()
>>> lm.rsquared
0.8971942610828956
>>> import numpy as np
>>> np.random.seed(12345)
>>> nums= np.random.rand(len(data))
>>> mask_large
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    mask_large
NameError: name 'mask_large' is not defined
>>> mask_large= nums > 0.5
>>> data['Size']= 'small'
>>> data.loc[mask_large,'Size']= 'large'
>>> data.head()
      TV  Radio  Newspaper  Sales   Size
0  230.1   37.8       69.2   22.1  large
1   44.5   39.3       45.1   10.4  small
2   17.2   45.9       69.3    9.3  small
3  151.5   41.3       58.5   18.5  small
4  180.8   10.8       58.4   12.9  large
>>> feature_cols= ['TV', 'Radio', 'Newspaper', 'IsLarge']
>>> X= data[feature_cols]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    X= data[feature_cols]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/frame.py", line 3512, in __getitem__
    indexer = self.columns._get_indexer_strict(key, "columns")[1]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5782, in _get_indexer_strict
    self._raise_if_missing(keyarr, indexer, axis_name)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5845, in _raise_if_missing
    raise KeyError(f"{not_found} not in index")
KeyError: "['IsLarge'] not in index"
>>> data['IsLarge']= data.Size.map({'small':0,'large':1})
>>> data.head()
      TV  Radio  Newspaper  Sales   Size  IsLarge
0  230.1   37.8       69.2   22.1  large        1
1   44.5   39.3       45.1   10.4  small        0
2   17.2   45.9       69.3    9.3  small        0
3  151.5   41.3       58.5   18.5  small        0
4  180.8   10.8       58.4   12.9  large        1
>>> feature_cols= ['TV', 'Radio', 'Newspaper', 'IsLarge']
>>> X= data[feature_cols]
>>> y= data.Sales
>>> lm= LinearRegression()
>>> lm.fit(X,y)
LinearRegression()
>>> zip(feature_cols,lm.coef_)
<zip object at 0x7fa8fa8cae00>
>>> np.random.seed(123456)
>>> nums= np.random.rand(len(data))
>>> mask_subirban= (nums > 0.33) & (nums < 0.66)
>>> data['Area']= 'rural'
>>> data.loc[mask_suburban,'Area']= 'suburban'
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    data.loc[mask_suburban,'Area']= 'suburban'
NameError: name 'mask_suburban' is not defined
>>> data.loc[mask_subirban,'Area']= 'suburban'
>>> mask_urban= nums > 0.66
>>> data.loc[mask_urban,'Area']= 'urban'
>>> data.head()
      TV  Radio  Newspaper  Sales   Size  IsLarge      Area
0  230.1   37.8       69.2   22.1  large        1     rural
1   44.5   39.3       45.1   10.4  small        0     urban
2   17.2   45.9       69.3    9.3  small        0     rural
3  151.5   41.3       58.5   18.5  small        0     urban
4  180.8   10.8       58.4   12.9  large        1  suburban
>>> area_dummies= pd.get_dummies(data.Area,prefix='Area').iloc[:,1:]
>>> data= pd.concat([data,area_dummies],axis=1)
>>> data.head()
      TV  Radio  Newspaper  Sales  ... IsLarge      Area Area_suburban  Area_urban
0  230.1   37.8       69.2   22.1  ...       1     rural             0           0
1   44.5   39.3       45.1   10.4  ...       0     urban             0           1
2   17.2   45.9       69.3    9.3  ...       0     rural             0           0
3  151.5   41.3       58.5   18.5  ...       0     urban             0           1
4  180.8   10.8       58.4   12.9  ...       1  suburban             1           0

[5 rows x 9 columns]
>>> feature_cols= ['TV', 'Radio', 'Newspaper', 'IsLarge', 'Area_suburban', 'Area_urban']
>>> X= data[feature_cols]
>>> y= data.Sales
>>> lm= LinearRegression()
>>> lm.fit(X,y)
LinearRegression()
>>> print(feature_cols,lm.coef_)
['TV', 'Radio', 'Newspaper', 'IsLarge', 'Area_suburban', 'Area_urban'] [ 0.04574401  0.1878667  -0.0010877   0.07739661 -0.10656299  0.26813802]
>>> 