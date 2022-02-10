Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> import os
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> df= pd.read_csv('Salaries.csv')

Warning (from warnings module):
  File "<pyshell#5>", line 1
DtypeWarning: Columns (12) have mixed types. Specify dtype option on import or set low_memory=False.
>>> df= pd.read_csv('Salaries.csv', low_memory= False)
>>> df.shape
(148648, 13)
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 148648 entries, 0 to 148647
Data columns (total 13 columns):
 #   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   Id                148648 non-null  int64  
 1   EmployeeName      148648 non-null  object 
 2   JobTitle          148648 non-null  object 
 3   BasePay           148043 non-null  float64
 4   OvertimePay       148648 non-null  float64
 5   OtherPay          148648 non-null  float64
 6   Benefits          112490 non-null  float64
 7   TotalPay          148648 non-null  float64
 8   TotalPayBenefits  148648 non-null  float64
 9   Year              148648 non-null  int64  
 10  Notes             0 non-null       float64
 11  Agency            148648 non-null  object 
 12  Status            38119 non-null   object 
dtypes: float64(7), int64(2), object(4)
memory usage: 14.7+ MB
>>> df.describe
<bound method NDFrame.describe of             Id       EmployeeName  ...         Agency  Status
0            1     NATHANIEL FORD  ...  San Francisco     NaN
1            2       GARY JIMENEZ  ...  San Francisco     NaN
2            3     ALBERT PARDINI  ...  San Francisco     NaN
3            4  CHRISTOPHER CHONG  ...  San Francisco     NaN
4            5    PATRICK GARDNER  ...  San Francisco     NaN
...        ...                ...  ...            ...     ...
148643  148646   Carolyn A Wilson  ...  San Francisco      PT
148644  148648     Joann Anderson  ...  San Francisco      PT
148645  148649        Leon Walker  ...  San Francisco      PT
148646  148650      Roy I Tillery  ...  San Francisco      PT
148647  148654          Joe Lopez  ...  San Francisco      PT

[148648 rows x 13 columns]>
>>> df.dtypes
Id                    int64
EmployeeName         object
JobTitle             object
BasePay             float64
OvertimePay         float64
OtherPay            float64
Benefits            float64
TotalPay            float64
TotalPayBenefits    float64
Year                  int64
Notes               float64
Agency               object
Status               object
dtype: object
>>> df.sort_values(by=['Total Pay'], acending=False)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    df.sort_values(by=['Total Pay'], acending=False)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
TypeError: sort_values() got an unexpected keyword argument 'acending'
>>> df.sort_values(by=['Total Pay'], ascending=False)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    df.sort_values(by=['Total Pay'], ascending=False)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/frame.py", line 6315, in sort_values
    k = self._get_label_or_level_values(by, axis=axis)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 1848, in _get_label_or_level_values
    raise KeyError(key)
KeyError: 'Total Pay'
>>> df.sort_values(by=['TotalPay'], ascending=False)
            Id        EmployeeName  ...         Agency  Status
0            1      NATHANIEL FORD  ...  San Francisco     NaN
1            2        GARY JIMENEZ  ...  San Francisco     NaN
110529  110532         David Shinn  ...  San Francisco      PT
110530  110533          Amy P Hart  ...  San Francisco      FT
36158    36160      Gary Altenberg  ...  San Francisco     NaN
...        ...                 ...  ...            ...     ...
106750  106753        Rita E Ortiz  ...  San Francisco     NaN
106749  106752     Cornelius  Hall  ...  San Francisco     NaN
106748  106751    Richard A Soares  ...  San Francisco     NaN
106747  106750  Richard P Matthews  ...  San Francisco     NaN
148647  148654           Joe Lopez  ...  San Francisco      PT

[148648 rows x 13 columns]
>>> pay_2011 = df.query("Year == 2011")['TotalPay'].sum()
>>> pay_2011
2594113030.72
>>> pay_2014 = df.query("Year == 2014")['TotalPay'].sum()
>>> pay_2014
2876910951.2599998
>>> subtact= pay_2014 - pay_2011
>>> subtact
282797920.53999996
>>> df_2011 = df[df['Year'] == 2011]
>>> df_2012 = df[df['Year'] == 2012]
>>> df_2013 = df[df['Year'] == 2013]
>>> df_2014 = df[df['Year'] == 2014]
>>> df_2011_top_employee = df_2011[['TotalPay','EmployeeName','JobTitle']].sort_values(by=['TotalPay'], ascending=False).head(1)
>>> df_2011_top_employee
    TotalPay    EmployeeName                                        JobTitle
0  567595.43  NATHANIEL FORD  GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY
>>> 