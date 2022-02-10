Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import pandas as pd
i
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> import warnings
>>> import seaborn as sns
>>> import os
>>> warnings.filterwarnings('ignore')
>>> plt.rcParams['figure.figsize']= (12,6)
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> df= pd.read_csv('driver-data.csv')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    df= pd.read_csv('driver-data.csv')
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 680, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 575, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 933, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 1217, in _make_engine
    self.handles = get_handle(  # type: ignore[call-overload]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/common.py", line 789, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'driver-data.csv'
>>> df= pd.read_csv('driver-data.csv')
>>> df.head()
           id  mean_dist_day  mean_over_speed_perc
0  3423311935          71.24                    28
1  3423313212          52.53                    25
2  3423313724          64.54                    27
3  3423311373          55.69                    22
4  3423310999          54.58                    25
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4000 entries, 0 to 3999
Data columns (total 3 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   id                    4000 non-null   int64  
 1   mean_dist_day         4000 non-null   float64
 2   mean_over_speed_perc  4000 non-null   int64  
dtypes: float64(1), int64(2)
memory usage: 93.9 KB
>>> df.describe()
                 id  mean_dist_day  mean_over_speed_perc
count  4.000000e+03    4000.000000           4000.000000
mean   3.423312e+09      76.041522             10.721000
std    1.154845e+03      53.469563             13.708543
min    3.423310e+09      15.520000              0.000000
25%    3.423311e+09      45.247500              4.000000
50%    3.423312e+09      53.330000              6.000000
75%    3.423313e+09      65.632500              9.000000
max    3.423314e+09     244.790000            100.000000
>>> from sklearn.cluster import KMeans
>>> kmeans= Kmeans(n_clusters=2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    kmeans= Kmeans(n_clusters=2)
NameError: name 'Kmeans' is not defined
>>> kmeans= KMeans(n_clusters=2)
>>> df_analyze= dr.drop('id',axis=1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    df_analyze= dr.drop('id',axis=1)
NameError: name 'dr' is not defined
>>> df_analyze= df.drop('id',axis=1)
>>> kmeans.fit(df_analyze)
KMeans(n_clusters=2)
>>> kmeans.cluster_centers_
array([[ 50.04763438,   8.82875   ],
       [180.017075  ,  18.29      ]])
>>> print(kmeans.labels_)
[0 0 0 ... 1 1 1]
>>> print(len(kmeans.labels_))
4000
>>> print(kmeans.labels_))
SyntaxError: unmatched ')'
>>> print(type(kmeans.labels_))
<class 'numpy.ndarray'>
>>> unique,counts= np.unique(kmeans.labels_,return_counts=True)
>>> print(dict)
<class 'dict'>
>>> print(dict(zip(unique,counts)))
{0: 3200, 1: 800}
>>> df_analyze['cluster']= kmeans.labels_
>>> sns.set_style('whitegrid')
>>> sns.lmplot('mean_dist_day','mean_over_speed_perc',data=df_analyze,hue='cluster',palette='coolwarm',size=6,aspect=1,fit_reg=False)
<seaborn.axisgrid.FacetGrid object at 0x7f86958247c0>
>>> plt.show()
>>> kmeans_4= KMEans(n_clusters=4)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    kmeans_4= KMEans(n_clusters=4)
NameError: name 'KMEans' is not defined
>>> kmeans_4= KMeans(n_clusters=4)
>>> kmeans_4.fit(df.drop('id', axis=1))
KMeans(n_clusters=4)
>>> kmeans_4.fit(df.drop('id', axis=1))
KMeans(n_clusters=4)
>>> print(kmeans_4.cluster_centersd)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(kmeans_4.cluster_centersd)
AttributeError: 'KMeans' object has no attribute 'cluster_centersd'
>>> print(kmeans_4.cluster_centers_)
[[ 49.9799964    5.22434282]
 [180.34311782  10.52011494]
 [177.83509615  70.28846154]
 [ 50.49167849  32.49172577]]
>>> unique,counts= np.unique(kmeans_4.labels_,return_counts=True)
>>> kmeans_4.cluster_centers_
array([[ 49.9799964 ,   5.22434282],
       [180.34311782,  10.52011494],
       [177.83509615,  70.28846154],
       [ 50.49167849,  32.49172577]])
>>> print(dict(zip(unique,counts)))
{0: 2775, 1: 696, 2: 104, 3: 425}
>>> df_analyze['cluster']=kmeans_4.labels_
>>> sns.set_style('whitegrid')
>>>  sns.lmplot('mean_dist_day','mean_over_speed_perc',data=df_analyze,hue='cluster',palette='coolwarm',size=6,aspect=1,fit_reg=False)
 
SyntaxError: unexpected indent
>>> sns.lmplot('mean_dist_day','mean_over_speed_perc',data=df_analyze,hue='cluster',palette='coolwarm',size=6,aspect=1,fit_reg=False)
<seaborn.axisgrid.FacetGrid object at 0x7f86958240d0>
>>> plt.show()
