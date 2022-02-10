Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import os
>>> import numpy as np
>>> import pandas as pd
>>> from sklearn import model_selection
>>> from sklearn.ensemble import AdaBoostClassifier
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> df= pd.read_csv('diabetes.csv')
>>> array= df.values
>>> X= array[:,0:8]
>>> Y= array[:,8]
>>> seed= 7
>>> num_trees= 30
>>> kfold= model_selection.KFold(n_splits=10, random_state=seed)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    kfold= model_selection.KFold(n_splits=10, random_state=seed)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/model_selection/_split.py", line 435, in __init__
    super().__init__(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/model_selection/_split.py", line 296, in __init__
    raise ValueError(
ValueError: Setting a random_state has no effect since shuffle is False. You should leave random_state to its default (None), or set shuffle=True.
>>> kfold= model_selection.KFold(n_splits=10, random_state=seed, shuffle= True)
>>> model= AdaBoostClassifier(n_estimators=num_trees,random_state=seed)
>>> results= model_selection.cross_val_score(model,X,Y,cv=kfold)
>>> print(results.mean())
0.7552802460697198
>>> from sklearn import svm
>>> from xgboost import XGBClassifier()
SyntaxError: invalid syntax
>>> from xgboost import XGBClassifier
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    from xgboost import XGBClassifier
ModuleNotFoundError: No module named 'xgboost'
>>> from xgboost import XGBClassifier

Warning (from warnings module):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/compat.py", line 36
    from pandas import MultiIndex, Int64Index
FutureWarning: pandas.Int64Index is deprecated and will be removed from pandas in a future version. Use pandas.Index with the appropriate dtype instead.
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    from xgboost import XGBClassifier
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/__init__.py", line 9, in <module>
    from .core import DMatrix, DeviceQuantileDMatrix, Booster, DataIter
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/core.py", line 203, in <module>
    _LIB = _load_lib()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/core.py", line 181, in _load_lib
    raise XGBoostError(
xgboost.core.XGBoostError: 
XGBoost Library (libxgboost.dylib) could not be loaded.
Likely causes:
  * OpenMP runtime is not installed
    - vcomp140.dll or libgomp-1.dll for Windows
    - libomp.dylib for Mac OSX
    - libgomp.so for Linux and other UNIX-like OSes
    Mac OSX users: Run `brew install libomp` to install OpenMP runtime.

  * You are running 32-bit Python on a 64-bit OS

Error message(s): ["dlopen(/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/lib/libxgboost.dylib, 0x0006): Library not loaded: /usr/local/opt/libomp/lib/libomp.dylib\n  Referenced from: /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/lib/libxgboost.dylib\n  Reason: tried: '/Applications/Python 3.9/IDLE.app/Contents/Frameworks/libomp.dylib' (no such file), '/usr/local/opt/libomp/lib/libomp.dylib' (no such file), '/usr/lib/libomp.dylib' (no such file)"]

>>> import warnings
>>> warnings.filterwarnings('ignore')
>>> from xgboost import XGBClassifier
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    from xgboost import XGBClassifier
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/__init__.py", line 9, in <module>
    from .core import DMatrix, DeviceQuantileDMatrix, Booster, DataIter
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/core.py", line 203, in <module>
    _LIB = _load_lib()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/core.py", line 181, in _load_lib
    raise XGBoostError(
xgboost.core.XGBoostError: 
XGBoost Library (libxgboost.dylib) could not be loaded.
Likely causes:
  * OpenMP runtime is not installed
    - vcomp140.dll or libgomp-1.dll for Windows
    - libomp.dylib for Mac OSX
    - libgomp.so for Linux and other UNIX-like OSes
    Mac OSX users: Run `brew install libomp` to install OpenMP runtime.

  * You are running 32-bit Python on a 64-bit OS

Error message(s): ["dlopen(/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/lib/libxgboost.dylib, 0x0006): Library not loaded: /usr/local/opt/libomp/lib/libomp.dylib\n  Referenced from: /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/lib/libxgboost.dylib\n  Reason: tried: '/Applications/Python 3.9/IDLE.app/Contents/Frameworks/libomp.dylib' (no such file), '/usr/local/opt/libomp/lib/libomp.dylib' (no such file), '/usr/lib/libomp.dylib' (no such file)"]

>>> from xgboost import XGBClassifier
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    from xgboost import XGBClassifier
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/__init__.py", line 9, in <module>
    from .core import DMatrix, DeviceQuantileDMatrix, Booster, DataIter
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/core.py", line 203, in <module>
    _LIB = _load_lib()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/core.py", line 181, in _load_lib
    raise XGBoostError(
xgboost.core.XGBoostError: 
XGBoost Library (libxgboost.dylib) could not be loaded.
Likely causes:
  * OpenMP runtime is not installed
    - vcomp140.dll or libgomp-1.dll for Windows
    - libomp.dylib for Mac OSX
    - libgomp.so for Linux and other UNIX-like OSes
    Mac OSX users: Run `brew install libomp` to install OpenMP runtime.

  * You are running 32-bit Python on a 64-bit OS

Error message(s): ["dlopen(/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/lib/libxgboost.dylib, 0x0006): Library not loaded: /usr/local/opt/libomp/lib/libomp.dylib\n  Referenced from: /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/xgboost/lib/libxgboost.dylib\n  Reason: tried: '/Applications/Python 3.9/IDLE.app/Contents/Frameworks/libomp.dylib' (no such file), '/usr/local/opt/libomp/lib/libomp.dylib' (no such file), '/usr/lib/libomp.dylib' (no such file)"]

>>> from xgboost import XGBClassifier
        