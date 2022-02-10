Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> from sklearn.model_selection import train_test_split
>>> import os
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/MachineLearning')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/MachineLearning')
FileNotFoundError: [Errno 2] No such file or directory: '/Users/robertogarcia/Documents/Ciencia de Datos/MachineLearning'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> loans= pd.read_csv(location)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    loans= pd.read_csv(location)
NameError: name 'location' is not defined
>>> loans= pd.read_csv("loan_borowwer_data.csv")
>>> loans.head()
   credit.policy             purpose  ...  pub.rec  not.fully.paid
0              1  debt_consolidation  ...        0               0
1              1         credit_card  ...        0               0
2              1  debt_consolidation  ...        0               0
3              1  debt_consolidation  ...        0               0
4              1         credit_card  ...        0               0

[5 rows x 14 columns]
>>> loans.tail()
      credit.policy             purpose  ...  pub.rec  not.fully.paid
9573              0           all_other  ...        0               1
9574              0           all_other  ...        0               1
9575              0  debt_consolidation  ...        0               1
9576              0    home_improvement  ...        0               1
9577              0  debt_consolidation  ...        0               1

[5 rows x 14 columns]
>>> loans.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9578 entries, 0 to 9577
Data columns (total 14 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   credit.policy      9578 non-null   int64  
 1   purpose            9578 non-null   object 
 2   int.rate           9578 non-null   float64
 3   installment        9578 non-null   float64
 4   log.annual.inc     9578 non-null   float64
 5   dti                9578 non-null   float64
 6   fico               9578 non-null   int64  
 7   days.with.cr.line  9578 non-null   float64
 8   revol.bal          9578 non-null   int64  
 9   revol.util         9578 non-null   float64
 10  inq.last.6mths     9578 non-null   int64  
 11  delinq.2yrs        9578 non-null   int64  
 12  pub.rec            9578 non-null   int64  
 13  not.fully.paid     9578 non-null   int64  
dtypes: float64(6), int64(7), object(1)
memory usage: 1.0+ MB
>>> loans['purpose'].unique()
array(['debt_consolidation', 'credit_card', 'all_other',
       'home_improvement', 'small_business', 'major_purchase',
       'educational'], dtype=object)
>>> loans.describe()
       credit.policy     int.rate  ...      pub.rec  not.fully.paid
count    9578.000000  9578.000000  ...  9578.000000     9578.000000
mean        0.804970     0.122640  ...     0.062122        0.160054
std         0.396245     0.026847  ...     0.262126        0.366676
min         0.000000     0.060000  ...     0.000000        0.000000
25%         1.000000     0.103900  ...     0.000000        0.000000
50%         1.000000     0.122100  ...     0.000000        0.000000
75%         1.000000     0.140700  ...     0.000000        0.000000
max         1.000000     0.216400  ...     5.000000        1.000000

[8 rows x 13 columns]
>>> loans.columns
Index(['credit.policy', 'purpose', 'int.rate', 'installment', 'log.annual.inc',
       'dti', 'fico', 'days.with.cr.line', 'revol.bal', 'revol.util',
       'inq.last.6mths', 'delinq.2yrs', 'pub.rec', 'not.fully.paid'],
      dtype='object')
>>> plt.figure(figsize=(10,6))
<Figure size 2000x1200 with 0 Axes>
>>> oans[loans['credit.policy']==1]['fico'].hist(alpha=0.5,color='blue',bins=30,label='credit.policy=1')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    oans[loans['credit.policy']==1]['fico'].hist(alpha=0.5,color='blue',bins=30,label='credit.policy=1')
NameError: name 'oans' is not defined
>>> loans[loans['credit.policy']==1]['fico'].hist(alpha=0.5,color='blue',bins=30,label='credit.policy=1')
<AxesSubplot:>
>>> loans[loans['credit.policy']==0]['fico'].hist(alpha=0.5,color='red',bins=30,label='credit.policy=0')
<AxesSubplot:>
>>> plt.legend()
<matplotlib.legend.Legend object at 0x7fb1f73287c0>
>>> plt.xlabel('FICO')
Text(0.5, 0, 'FICO')
>>> plt.show()
>>> plt.figure(figsize=(10,6))
<Figure size 2000x1200 with 0 Axes>
>>> loans[loans['not.fully.paid']==1]['fico'].hist(alpha=0.5,color='blue',bins=30,label='not.fully.paid=1')
<AxesSubplot:>
>>> loans[loans['not.fully.paid']==0]['fico'].hist(alpha=0.5,color='red',bins=30,label='not.fully.paid=0')
<AxesSubplot:>
>>> plt.legend()
<matplotlib.legend.Legend object at 0x7fb1fd004820>
>>> plt.xlabel('FICO')
Text(0.5, 0, 'FICO')
>>> df=loans.copy()
>>> df
      credit.policy             purpose  ...  pub.rec  not.fully.paid
0                 1  debt_consolidation  ...        0               0
1                 1         credit_card  ...        0               0
2                 1  debt_consolidation  ...        0               0
3                 1  debt_consolidation  ...        0               0
4                 1         credit_card  ...        0               0
...             ...                 ...  ...      ...             ...
9573              0           all_other  ...        0               1
9574              0           all_other  ...        0               1
9575              0  debt_consolidation  ...        0               1
9576              0    home_improvement  ...        0               1
9577              0  debt_consolidation  ...        0               1

[9578 rows x 14 columns]
>>> df.rename(columns={'not.fully.paid':'not_fully_paid'},inplace=True)
>>> df
      credit.policy             purpose  ...  pub.rec  not_fully_paid
0                 1  debt_consolidation  ...        0               0
1                 1         credit_card  ...        0               0
2                 1  debt_consolidation  ...        0               0
3                 1  debt_consolidation  ...        0               0
4                 1         credit_card  ...        0               0
...             ...                 ...  ...      ...             ...
9573              0           all_other  ...        0               1
9574              0           all_other  ...        0               1
9575              0  debt_consolidation  ...        0               1
9576              0    home_improvement  ...        0               1
9577              0  debt_consolidation  ...        0               1

[9578 rows x 14 columns]
>>> labels = 'FULLY PAID','NOT FULLY PAID'
>>> sizes = [df.not_fully_paid[df['not_fully_paid']==0].count(), df.not_fully_paid[df['not_fully_paid']==1].count()]
>>> explode = (0, 0.1)
>>> fig1, ax1 = plt.subplots(figsize=(10, 8))
>>> ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
([<matplotlib.patches.Wedge object at 0x7fb1fd07a6d0>, <matplotlib.patches.Wedge object at 0x7fb1fd1d8a30>], [Text(-0.5300933688271362, -0.9638469901003468, 'FULLY PAID'), Text(0.5782835766384721, 1.0514694978886532, 'NOT FULLY PAID')], [Text(-0.28914183754207423, -0.5257347218729164, '84.0%'), Text(0.33733208637244205, 0.6133572071017144, '16.0%')])
>>> ax1.axis('equal')
(-1.106134809663821, 1.1065119019520544, -1.1095650881563976, 1.192250469605276)
>>> plt.title("Proportion of customer with fully paid and fully not paid", size = 20)
Text(0.5, 1.0, 'Proportion of customer with fully paid and fully not paid')
>>> plt.show()
>>> labels = df['purpose'].astype('category').cat.categories.tolist()
>>> counts = df['purpose'].value_counts()
>>> sizes = [counts[var_cat] for var_cat in labels]
>>> fig1, ax1 = plt.subplots()
>>> explode = (0.1, 0, 0, 0, 0,0,0)
>>> ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
([<matplotlib.patches.Wedge object at 0x7fb1fd45c610>, <matplotlib.patches.Wedge object at 0x7fb1fd45cfa0>, <matplotlib.patches.Wedge object at 0x7fb1fd46b970>, <matplotlib.patches.Wedge object at 0x7fb1fd47a340>, <matplotlib.patches.Wedge object at 0x7fb1fd47acd0>, <matplotlib.patches.Wedge object at 0x7fb1fd64d6a0>, <matplotlib.patches.Wedge object at 0x7fb1fd65b070>], [Text(0.7938480171222339, 0.7614494899276627, 'all_other'), Text(-0.4001152463281499, 1.0246500815672461, 'credit_card'), Text(-0.958230075669315, -0.5401806383819947, 'debt_consolidation'), Text(0.3802125532973449, -1.032200762601498, 'educational'), Text(0.6845888715509435, -0.8610099168700707, 'home_improvement'), Text(0.9381209474652868, -0.5743945403003347, 'major_purchase'), Text(1.077405568028621, -0.22180451298592804, 'small_business')], [Text(0.43300800933940026, 0.4153360854150887, '24.3%'), Text(-0.21824467981535445, 0.5589000444912251, '13.2%'), Text(-0.5226709503650808, -0.2946439845719971, '41.3%'), Text(0.20738866543491535, -0.5630185977826352, '3.6%'), Text(0.37341211175506006, -0.4696417728382203, '6.6%'), Text(0.5117023349810654, -0.31330611289109156, '4.6%'), Text(0.5876757643792477, -0.12098427981050619, '6.5%')])
>>> ax1.axis('equal')
(-1.1213354685636516, 1.1010159780154343, -1.1245973020230766, 1.106303536803432)
>>> plt.show()
>>> loans.head()
   credit.policy             purpose  ...  pub.rec  not.fully.paid
0              1  debt_consolidation  ...        0               0
1              1         credit_card  ...        0               0
2              1  debt_consolidation  ...        0               0
3              1  debt_consolidation  ...        0               0
4              1         credit_card  ...        0               0

[5 rows x 14 columns]
>>> plt.figure(figsize=(11,7))
<Figure size 2200x1400 with 0 Axes>
>>> sns.countplot(x='purpose',hue='not.fully.paid',data=loans,palette='Set1')
<AxesSubplot:xlabel='purpose', ylabel='count'>
>>> plt.figure(figsize=(11,7))
<Figure size 2200x1400 with 0 Axes>
>>> sns.countplot(x='purpose',hue='not.fully.paid',data=loans)
<AxesSubplot:xlabel='purpose', ylabel='count'>
>>> cat_feats=['purpose']
>>> cat_feats
['purpose']
>>> final_data=pd.get_dummies(loans,columns=cat_feats,drop_first=True)
>>> final_data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9578 entries, 0 to 9577
Data columns (total 19 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   credit.policy               9578 non-null   int64  
 1   int.rate                    9578 non-null   float64
 2   installment                 9578 non-null   float64
 3   log.annual.inc              9578 non-null   float64
 4   dti                         9578 non-null   float64
 5   fico                        9578 non-null   int64  
 6   days.with.cr.line           9578 non-null   float64
 7   revol.bal                   9578 non-null   int64  
 8   revol.util                  9578 non-null   float64
 9   inq.last.6mths              9578 non-null   int64  
 10  delinq.2yrs                 9578 non-null   int64  
 11  pub.rec                     9578 non-null   int64  
 12  not.fully.paid              9578 non-null   int64  
 13  purpose_credit_card         9578 non-null   uint8  
 14  purpose_debt_consolidation  9578 non-null   uint8  
 15  purpose_educational         9578 non-null   uint8  
 16  purpose_home_improvement    9578 non-null   uint8  
 17  purpose_major_purchase      9578 non-null   uint8  
 18  purpose_small_business      9578 non-null   uint8  
dtypes: float64(6), int64(7), uint8(6)
memory usage: 1.0 MB
>>> final_data.describe()
       credit.policy  ...  purpose_small_business
count    9578.000000  ...             9578.000000
mean        0.804970  ...                0.064627
std         0.396245  ...                0.245880
min         0.000000  ...                0.000000
25%         1.000000  ...                0.000000
50%         1.000000  ...                0.000000
75%         1.000000  ...                0.000000
max         1.000000  ...                1.000000

[8 rows x 19 columns]
>>> X=final_data.drop('not.fully.paid',axis=1)
>>> X.describe()
       credit.policy  ...  purpose_small_business
count    9578.000000  ...             9578.000000
mean        0.804970  ...                0.064627
std         0.396245  ...                0.245880
min         0.000000  ...                0.000000
25%         1.000000  ...                0.000000
50%         1.000000  ...                0.000000
75%         1.000000  ...                0.000000
max         1.000000  ...                1.000000

[8 rows x 18 columns]
>>> y= final_data['not.fully.paid']
>>> y
0       0
1       0
2       0
3       0
4       0
       ..
9573    1
9574    1
9575    1
9576    1
9577    1
Name: not.fully.paid, Length: 9578, dtype: int64
>>> X=final_data.drop('not.fully.paid',axis=1)
>>> y = final_data['not.fully.paid']
>>> X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=101)
>>> from sklearn.tree import DecisionTreeClassifier
>>> dtree=DecisionTreeClassifier()
>>> dtree.fit(X_train,y_train)
DecisionTreeClassifier()
>>> predictions=dtree.predict(X_test)
>>> from sklearn.metrics import classification_report,confusion_matrix
>>> print(classification_report(y_test,predictions))
              precision    recall  f1-score   support

           0       0.86      0.81      0.83      2431
           1       0.19      0.25      0.22       443

    accuracy                           0.73      2874
   macro avg       0.52      0.53      0.53      2874
weighted avg       0.75      0.73      0.74      2874

>>> print(confusion_matrix(y_test,predictions))
[[1978  453]
 [ 334  109]]
>>> from sklearn.ensemble import RandomForestClassifier
>>> rfc=RandomForestClassifier(n_estimators=600)
>>> rfc.fit(X_train,y_train)
RandomForestClassifier(n_estimators=600)
predictions=dtree.predict(X_test)
>>> from sklearn.metrics import classification_report,confusion_matrix
>>> print(classification_report(y_test,predictions))
              precision    recall  f1-score   support

           0       0.86      0.81      0.83      2431
           1       0.19      0.25      0.22       443

    accuracy                           0.73      2874
   macro avg       0.52      0.53      0.53      2874
weighted avg       0.75      0.73      0.74      2874

>>> from sklearn.ensemble import GradientBoostingClassifier
>>> from sklearn.model_selection import GridSearchCV
>>> parameters = {
   "loss":["deviance"],
    "learning_rate": [0.01, 0.025, 0.05, 0.075, 0.1, 0.15, 0.2],
    "min_samples_split": np.linspace(0.1, 0.5, 12),
    "min_samples_leaf": np.linspace(0.1, 0.5, 12),
    "max_depth":[3,5,8,10],
    "max_features":["log2","sqrt"],
    "criterion": ["friedman_mse",  "mae"],
    "subsample":[0.5, 0.618, 0.8, 0.85, 0.9, 0.95, 1.0],
    "n_estimators":[10]
    }
>>> gb_clf = GridSearchCV(GradientBoostingClassifier(), parameters, cv=5, n_jobs=-1,verbose=1)
>>> gb_clf.fit(X_train, y_train)
Fitting 5 folds for each of 112896 candidates, totalling 564480 fits
