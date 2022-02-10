Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import os
>>> import pandas as pd
i
>>> import numpy as np
>>> import matplotlib
>>> import matplotlib.pyplot as plt
>>> form pandas.plotting import scatter_matrix
SyntaxError: invalid syntax
>>> from pandas.plotting import scatter_matrix
>>> import seaborn as sns
sns.
>>> sns.set(style="white",color_codes=True)
>>> sns.set(font_scale=1.5)
>>> from sklearn.linear_model import LogisticRegression
>>> from sklearn.model_selection import train_test_split
>>> from sklearn.metrics import confusion_matrix
>>> from sklearn.metrics import classification_report
>>> from sklearn.metrics import accuracy_score
>>> from sklearn.metrics import precision_score
>>> from sklearn.metrics import recall_score
>>> from sklearn.metrics import f1_score
>>> from sklearn.metrics import metrics
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    from sklearn.metrics import metrics
ImportError: cannot import name 'metrics' from 'sklearn.metrics' (/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/metrics/__init__.py)
>>> from sklearn.metrics import warninga
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    from sklearn.metrics import warninga
ImportError: cannot import name 'warninga' from 'sklearn.metrics' (/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/metrics/__init__.py)
>>> from sklearn.metrics import warnings
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    from sklearn.metrics import warnings
ImportError: cannot import name 'warnings' from 'sklearn.metrics' (/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/metrics/__init__.py)
>>> from sklearn import metrics
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> df_train= pd.read_csv('train.csv')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    df_train= pd.read_csv('train.csv')
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 680, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 575, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 933, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 1231, in _make_engine
    return mapping[engine](f, **self.options)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/c_parser_wrapper.py", line 75, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 544, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 633, in pandas._libs.parsers.TextReader._get_header
  File "pandas/_libs/parsers.pyx", line 847, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 1952, in pandas._libs.parsers.raise_parser_error
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xca in position 1163: invalid continuation byte
>>> df_train.shape
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    df_train.shape
NameError: name 'df_train' is not defined
>>> df_train= pd.read_csv('train.csv', index_col=0, sep';')
SyntaxError: positional argument follows keyword argument
>>> df_train= pd.read_csv('train.csv', index_col=0, sep=';')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    df_train= pd.read_csv('train.csv', index_col=0, sep=';')
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 680, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 575, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 933, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 1231, in _make_engine
    return mapping[engine](f, **self.options)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/c_parser_wrapper.py", line 75, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 544, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 633, in pandas._libs.parsers.TextReader._get_header
  File "pandas/_libs/parsers.pyx", line 847, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 1952, in pandas._libs.parsers.raise_parser_error
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xca in position 1163: invalid continuation byte
>>> df_train= pd.read_csv('train.csv', sep='|', names=m_cols , encoding='latin-1')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    df_train= pd.read_csv('train.csv', sep='|', names=m_cols , encoding='latin-1')
NameError: name 'm_cols' is not defined
>>> df_train= pd.read_csv('train.csv')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    df_train= pd.read_csv('train.csv')
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 680, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 575, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 933, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 1231, in _make_engine
    return mapping[engine](f, **self.options)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/c_parser_wrapper.py", line 75, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 544, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 633, in pandas._libs.parsers.TextReader._get_header
  File "pandas/_libs/parsers.pyx", line 847, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 1952, in pandas._libs.parsers.raise_parser_error
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xca in position 1163: invalid continuation byte
>>>  o.decode('latin-1').encode("utf-8")
 
SyntaxError: unexpected indent
>>> o.decode('latin-1').encode("utf-8")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    o.decode('latin-1').encode("utf-8")
NameError: name 'o' is not defined
>>> df_train= pd.read_csv('train.csv', encoding='latin-1')
>>> df_train.shape
(891, 11)
>>> df_train.Survided.value_counts()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    df_train.Survided.value_counts()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 5583, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Survided'
>>> df_train.Survived.value_counts()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    df_train.Survived.value_counts()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 5583, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Survived'
>>> df_train.Survived.value_counts()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    df_train.Survived.value_counts()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 5583, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Survived'
>>> df_train.Sex.value_counts()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    df_train.Sex.value_counts()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 5583, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Sex'
>>> df_train.survived.value_counts()
0    549
1    342
Name: survived, dtype: int64
>>> df_train.sex.value_counts()
male      577
female    314
Name: sex, dtype: int64
>>> df_train.embarked.value_counts()
S    644
C    168
Q     77
Name: embarked, dtype: int64
>>> df_train.isnull().sum()
survived      0
pclass        0
name          0
sex           0
age         177
sibsp         0
parch         0
ticket        0
fare          0
cabin       687
embarked      2
dtype: int64
>>> df_train.shape
(891, 11)
>>> df_train= dr_train.drop(['PassengerID','Name','Ticket','Cabin'], axis=1)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    df_train= dr_train.drop(['PassengerID','Name','Ticket','Cabin'], axis=1)
NameError: name 'dr_train' is not defined
>>> fr_train.head()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    fr_train.head()
NameError: name 'fr_train' is not defined
>>> df_train.head()
   survived  pclass  ... cabin embarked
0         0       3  ...   NaN        S
1         1       1  ...   C85        C
2         1       3  ...   NaN        S
3         1       1  ...  C123        S
4         0       3  ...   NaN        S

[5 rows x 11 columns]
>>> def age_approx(cols):
	Age= cols[0]
	Pclass= cols[1]

	
>>> def age_approx(cols):
	Age= cols[0]
	Pclass= cols[1]
	if pd.isnull(age):
		if Pclass == 1:
			elif Pclass == 2:
				
SyntaxError: invalid syntax
>>> def age_approx(cols):
	Age= cols[0]
	Pclass= cols[1]
	if pd.isnull(age):
		if Pclass ==1:
			elif Pclass ==2:
				
SyntaxError: invalid syntax
>>> def age_approx(cols):
	Age= cols[0]
	Pclass= cols[1]
	if pd.isnull(age):
		if Pclass ==1:
			return 37
		elif Pclass ==2:
			return 29
		else:
			return 24
	else:
		return Age

	
>>> df_train.groupby(['Pclass']).mean()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    df_train.groupby(['Pclass']).mean()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/frame.py", line 7714, in groupby
    return DataFrameGroupBy(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/groupby/groupby.py", line 882, in __init__
    grouper, exclusions, obj = get_grouper(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/groupby/grouper.py", line 882, in get_grouper
    raise KeyError(gpr)
KeyError: 'Pclass'
>>> df_train['age']= df_train[['age','Pclass']].apply(age_approx, axis=1)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    df_train['age']= df_train[['age','Pclass']].apply(age_approx, axis=1)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/frame.py", line 3512, in __getitem__
    indexer = self.columns._get_indexer_strict(key, "columns")[1]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5782, in _get_indexer_strict
    self._raise_if_missing(keyarr, indexer, axis_name)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5845, in _raise_if_missing
    raise KeyError(f"{not_found} not in index")
KeyError: "['Pclass'] not in index"
>>> df_train['age']= df_train[['age','pclass']].apply(age_approx, axis=1)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    df_train['age']= df_train[['age','pclass']].apply(age_approx, axis=1)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/frame.py", line 8827, in apply
    return op.apply().__finalize__(self, method="apply")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/apply.py", line 727, in apply
    return self.apply_standard()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/apply.py", line 851, in apply_standard
    results, res_index = self.apply_series_generator()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/apply.py", line 867, in apply_series_generator
    results[i] = self.f(v)
  File "<pyshell#75>", line 4, in age_approx
    if pd.isnull(age):
NameError: name 'age' is not defined
>>> def age_approx(cols):
	age= cols[0]
	pclass= cols[1]
	if pd.isnull(age):
		if pclass ==1:
			return 37
		elif pclass ==2:
			return 29
		else:
			return 24
	else:
		return age

>>> df_train.groupby(['pclass']).mean()
        survived        age     sibsp     parch       fare
pclass                                                    
1       0.629630  38.233441  0.416667  0.356481  84.154687
2       0.472826  29.877630  0.402174  0.380435  20.662183
3       0.242363  25.140620  0.615071  0.393075  13.675550
>>> df_train['age']= df_train[['age','pclass']].apply(age_approx, axis=1)
>>> df_train.isnull().sum()
survived      0
pclass        0
name          0
sex           0
age           0
sibsp         0
parch         0
ticket        0
fare          0
cabin       687
embarked      2
dtype: int64
>>> df_train.dropna(inplace=True)
>>> df_train.isnull().sum()
survived    0
pclass      0
name        0
sex         0
age         0
sibsp       0
parch       0
ticket      0
fare        0
cabin       0
embarked    0
dtype: int64
>>> df_train.dtypes
survived      int64
pclass        int64
name         object
sex          object
age         float64
sibsp         int64
parch         int64
ticket       object
fare        float64
cabin        object
embarked     object
dtype: object
>>> df_train_dummied= pd.get_dummies(df_train, columns=["Sex"])
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    df_train_dummied= pd.get_dummies(df_train, columns=["Sex"])
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/reshape/reshape.py", line 927, in get_dummies
    data_to_encode = data[columns]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/frame.py", line 3512, in __getitem__
    indexer = self.columns._get_indexer_strict(key, "columns")[1]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5782, in _get_indexer_strict
    self._raise_if_missing(keyarr, indexer, axis_name)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5842, in _raise_if_missing
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index(['Sex'], dtype='object')] are in the [columns]"
>>> df_train_dummied= pd.get_dummies(df_train, columns=["sex"])
>>> df_train_dummied= pd.get_dummies(df_train, columns=["embarked"])
>>> df_train_dummied.head()
    survived  pclass  ... embarked_Q embarked_S
1          1       1  ...          0          0
3          1       1  ...          0          1
6          0       1  ...          0          1
10         1       3  ...          0          1
11         1       1  ...          0          1

[5 rows x 13 columns]
>>> plt.figure(figsize= (6,4))
<Figure size 1200x800 with 0 Axes>
s
>>> sns.heatmap()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    sns.heatmap()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/seaborn/_decorators.py", line 46, in inner_f
    return f(**kwargs)
TypeError: heatmap() missing 1 required positional argument: 'data'
>>> sns.heatmap(df_train_dummied.corr())
<AxesSubplot:>
>>> plt.show()
>>> 