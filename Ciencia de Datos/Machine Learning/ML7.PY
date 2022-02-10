Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sklearn
>>> import sklearn.datasets import load_iris
SyntaxError: invalid syntax
>>> from sklearn.datasets import load_iris
>>> dta= load_iris()
>>> data= load_iris()
>>> x= data.iris
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/utils/__init__.py", line 117, in __getattr__
    return self[key]
KeyError: 'iris'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x= data.iris
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/utils/__init__.py", line 119, in __getattr__
    raise AttributeError(key)
AttributeError: iris
>>> y= data.target
>>> x= data.data
>>> from sklearn.model_selection import train_test_split
>>> x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=1)
>>> print(x_train.shape)
(120, 4)
>>> from sklearn.linear_model import LogisticRegression
>>> lr= LogisticRegression()
>>> 
>>> lr.fit(x_train, y_train)

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
>>> y_predict= lr.predict(x_test)
>>> from sklearn.metrics import accuracy_score
>>> accuracy= accuracy_score(y_predict,y_test)
>>> print(accuracy)
0.9666666666666667
>>> sklearn_pca= PCA(n_components=0.95)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sklearn_pca= PCA(n_components=0.95)
NameError: name 'PCA' is not defined
>>> from sklearn.decomposition import PCA
>>> sklearn_pca= PCA(n_components=0.95)
>>> sklearn_pca.fit(x_train)
PCA(n_components=0.95)
>>> x_train_transformed= sklearn_pca.transform(x_train)
>>> print(x_train_transformed.shape)
(120, 2)
>>> print(x_test.shape)
(30, 4)
>>> x_train_transformed= sklearn_pca.transform(x_test)
>>> x_test_transformed= sklearn_pca.transform(x_test)
>>> print(x_test_transformed.shape)
(30, 2)
>>> lr= LogisticRegression(penalty='l1')
>>> lr.fit(x_train_transformed,y_train)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    lr.fit(x_train_transformed,y_train)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/linear_model/_logistic.py", line 1461, in fit
    solver = _check_solver(self.solver, self.penalty, self.dual)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/linear_model/_logistic.py", line 447, in _check_solver
    raise ValueError(
ValueError: Solver lbfgs supports only 'l2' or 'none' penalties, got l1 penalty.
>>> lr= LogisticRegression(penalty='l2')
>>> lr.fit(x_train_transformed,y_train)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    lr.fit(x_train_transformed,y_train)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/linear_model/_logistic.py", line 1508, in fit
    X, y = self._validate_data(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/base.py", line 581, in _validate_data
    X, y = check_X_y(X, y, **check_params)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/utils/validation.py", line 981, in check_X_y
    check_consistent_length(X, y)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/utils/validation.py", line 332, in check_consistent_length
    raise ValueError(
ValueError: Found input variables with inconsistent numbers of samples: [30, 120]
>>> lr= LogisticRegression(penalty='l1')
>>> 