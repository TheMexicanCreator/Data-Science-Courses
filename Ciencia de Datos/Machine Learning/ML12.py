Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import numpy as np
>>> import pandas as pd
>>> from datetime import datetime as dt
>>> from statsmodels.tsa.stattoolst import adfuller, acf, pacf
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    from statsmodels.tsa.stattoolst import adfuller, acf, pacf
ModuleNotFoundError: No module named 'statsmodels.tsa.stattoolst'
>>> from statsmodels.tsa.stattoolst import adfuller, acf, pacf
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    from statsmodels.tsa.stattoolst import adfuller, acf, pacf
ModuleNotFoundError: No module named 'statsmodels.tsa.stattoolst'
>>> from statsmodels.tsa.stattoolst import adfuller, acf, pacf
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    from statsmodels.tsa.stattoolst import adfuller, acf, pacf
ModuleNotFoundError: No module named 'statsmodels.tsa.stattoolst'
>>> from statsmodels.tsa.arima_model import ARIMA
>>> import math
>>> import matplotlib.pyplot as plt
>>> from matplotlib.pylab import rcParams
>>> rcParams['figure.figsize']= 15,6
>>> import warnings
>>> warnings.filterwarnings('ignore')
>>> Que onda Pepe, si vas a poder ir a mi casa el domingo para ver el Superbowl?
SyntaxError: invalid syntax
>>> from statsmodels.tsa.stattoolst import adfuller, acf, pacf
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    from statsmodels.tsa.stattoolst import adfuller, acf, pacf
ModuleNotFoundError: No module named 'statsmodels.tsa.stattoolst'
>>> import statsmodels.tsa.stattoolst
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    import statsmodels.tsa.stattoolst
ModuleNotFoundError: No module named 'statsmodels.tsa.stattoolst'
>>> from statsmodels.tsa.stattools import adfuller, acf, pacf
>>> import os
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> data= pd.read_csv('AirPassengers.csv')
>>> data['Month'].head()
0    1949-01
1    1949-02
2    1949-03
3    1949-04
4    1949-05
Name: Month, dtype: object
>>> data['Month']= data['Month'].apply(lambda x: dt(int(x[:4]),int(x[5:]),15))
>>> data = data.set_index('Month')
>>> data.head()
            #Passengers
Month                  
1949-01-15          112
1949-02-15          118
1949-03-15          132
1949-04-15          129
1949-05-15          121
>>> ts= data['#Passengers']
>>> plt.plot(ts)
[<matplotlib.lines.Line2D object at 0x7fd4bf200fa0>]
>>> plt.show()
>>> ts_log= np.log(ts)
>>> def test_stationary(timeseries):
	rolmean= timeseries.rolling(window=52,center=False).mean()
	rolstd= timeseries.rolling(window=52,center=False).std()
	orig= plt.plot(timeseries,color='blue',label='Original')
	mean= plt.plot(rolmean,color='red',label='Rolling Mean')
	std= plt.plot(rolstd,color='black',label='Rolling Std')
	plt.legend(loc='best')
	plt.title('Rolling MEan & Standard Deviation')
	plt.show(block=False)
	print('Results of Dickey-Fuller Test:')
	dftest= adfuller(timeseries,autolag='AIC')
	dfoutput= pd.Series(dftest[0:4], index= ['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])

>>> for key,value in dftest[4].items():
	dfoutput['Critical Value (%s)' %key]= value

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    for key,value in dftest[4].items():
NameError: name 'dftest' is not defined
>>> print(dfoutput)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(dfoutput)
NameError: name 'dfoutput' is not defined
>>> def test_stationarity(timeseries):
	rolmean= timeseries.rolling(window=52,center=False).mean()
	rolstd= timeseries.rolling(window=52,center=False).std()

	
>>> def test_stationarity(timeseries):
	rolmean= timeseries.rolling(window=52,center=False).mean()
	rolstd= timeseries.rolling(window=52,center=False).std()
	orig= plt.plot(timeseries,color='blue',label='Original')
	mean= plt.plot(rolmean,color='red',label='Rolling Mean')
	std= plt.plot(rolstd,color='black',label='Rolling Std')
	plt.legend(loc='best')
	plt.title('Rolling Mean & Standard Deviation')
	plt.show(block=False)
	print('Results of Dickey-Fuller Test:')
	dftest= adfuller(timeseries,autolag='AIC')
	dfoutput= pd.Series(dftest[0:4], index= ['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])

	
>>> for key,value in dftest[4].items():
	dfoutput['Critical Value (%s)']= value

	
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    for key,value in dftest[4].items():
NameError: name 'dftest' is not defined
>>> print('Results of Dickey-Fuller Test:')
Results of Dickey-Fuller Test:
>>> dftest= adfuller(timeseries,autolag='AIC')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    dftest= adfuller(timeseries,autolag='AIC')
NameError: name 'timeseries' is not defined
>>> 
>>> #Ejercicio 2
>>> data= pd.read_csv('monthly-beer-production-in-austr.csv')
>>> data['Month'].head()
0    1956-01
1    1956-02
2    1956-03
3    1956-04
4    1956-05
Name: Month, dtype: object
>>>  data['Month']= data['Month'].apply(lambda x: dt(int(x[:4]),int(x[5:]),15))
 
SyntaxError: unexpected indent
>>> data['Month']= data['Month'].apply(lambda x: dt(int(x[:4]),int(x[5:]),15))
>>> data = data.set_index('Month')
>>> data.head()
            Monthly beer production in Australia
Month                                           
1956-01-15                                  93.2
1956-02-15                                  96.0
1956-03-15                                  95.2
1956-04-15                                  77.1
1956-05-15                                  70.9
>>> ts= data['Monthly beer production in Australia']
>>> plt.show()
>>> plt.plot(ts)
[<matplotlib.lines.Line2D object at 0x7fd4bf2641f0>]
>>> plt.show()
>>> ts_log= np.log(ts)
>>> 