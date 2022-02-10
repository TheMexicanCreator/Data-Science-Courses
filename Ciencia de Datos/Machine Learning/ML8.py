Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> from mlxtend.data import iris_data
>>> from mlxtend.preprocessing import standarize
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    from mlxtend.preprocessing import standarize
ImportError: cannot import name 'standarize' from 'mlxtend.preprocessing' (/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/mlxtend/preprocessing/__init__.py)
>>> from mlxtend.preprocessing import standardize
>>> from mlxtend.feature_extraction import LinearDiscriminantAnalysis
>>> X,y= iris_data()
>>> X= standardize(X)
>>> lda= LinearDisciminantAnalysis(n_discriminants=2)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    lda= LinearDisciminantAnalysis(n_discriminants=2)
NameError: name 'LinearDisciminantAnalysis' is not defined
>>> lda= LinearDiscriminantAnalysis(n_discriminants=2)
>>> lda.fit(X,y)
<mlxtend.feature_extraction.linear_discriminant_analysis.LinearDiscriminantAnalysis object at 0x7f9080f57070>
>>> X_lda= lda.transform(X)
>>> X_da
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    X_da
NameError: name 'X_da' is not defined
>>> X_lda

>>> 
>>> #Ejercicio 2
>>> import pandas as pd
>>> import numpy as np
>>> from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
>>> import matplotlib.pyplot as plt
>>> from sklearn.datasets import load_digits
>>> from sklearn.model_selection import train_test_split
>>> from sklearn.linear_model import LogisticRegression
>>> from sklearn import metrics
>>> digits= load_digits()
>>> plt.gray()
>>> plt.matshow(digits.images[0])
<matplotlib.image.AxesImage object at 0x7f908271c0a0>
>>> plt.show()
>>> images = digits.images.reshape(digits.images.shape[0], -1)
>>> labels= digits.target
>>> train_x, test_x, train_y, test_y = train_test_split(images, labels, random_state=10, test_size=0.20)
>>> model_lda= LDA(n_components=5)
>>> model_lda.fit(train_x, train_y)
LinearDiscriminantAnalysis(n_components=5)
>>> print(model_lda.explained_variance_ratio_)
[0.29115346 0.1856254  0.16536448 0.1171311  0.08263054]
>>> train_x = model_lda.transform(train_x)
>>> test_x= model_lda.transform(test_x)
>>> log_model = LogisticRegression()
>>> log_model.fit(train_x, train_y)

Warning (from warnings module):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/linear_model/_logistic.py", line 814
    n_iter_i = _check_optimize_result(
ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
LogisticRegression()
>>> redicted_values = log_model.predict(test_x)
>>> print("Accuracy Score\n")
Accuracy Score

>>> print(metrics.accuracy_score(predicted_values, test_y))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(metrics.accuracy_score(predicted_values, test_y))
NameError: name 'predicted_values' is not defined
>>> rint(metrics.accuracy_score(redicted_values, test_y))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    rint(metrics.accuracy_score(redicted_values, test_y))
NameError: name 'rint' is not defined
>>> print(metrics.accuracy_score(redicted_values, test_y))
0.9055555555555556
>>> print("\n\n")



>>> 