Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import seaborn as sns
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import seaborn as sns
ModuleNotFoundError: No module named 'seaborn'
>>> import seaborn as sns
>>> import numpy as np
>>> import pandas as pd
>>> sns.set()
>>> rng= np.random.RandomState(0)
>>> x= np.linspace(0,10,500)
>>> y= np.cumsum(rng.randn(500,6),0)
>>> plt.`plot(x,y)
SyntaxError: invalid syntax
>>> plt.plot(x,y)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    plt.plot(x,y)
NameError: name 'plt' is not defined
>>> import matplotlib as plt
>>> plt.style.use('classic')
>>> %matplotlib inline
SyntaxError: invalid syntax
>>> plt.plot(x,y)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    plt.plot(x,y)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/_api/__init__.py", line 222, in __getattr__
    raise AttributeError(
AttributeError: module 'matplotlib' has no attribute 'plot'
>>> import matplotlib.pyplot as plt
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x7fdbd8fa7760>, <matplotlib.lines.Line2D object at 0x7fdbd8fa7700>, <matplotlib.lines.Line2D object at 0x7fdbd8fa7820>, <matplotlib.lines.Line2D object at 0x7fdbd8fa7940>, <matplotlib.lines.Line2D object at 0x7fdbd8fa7a60>, <matplotlib.lines.Line2D object at 0x7fdbd8fa7b80>]
>>> plt.legend('ABCDEF', ncol=2, loc='upper left')
<matplotlib.legend.Legend object at 0x7fdbd8dfc5b0>
>>> 
>>> #Ejercicio 2
>>> import seaborn as sns
>>> data= sns.load_dataset("iris")
>>> sns.lineplot(x="sepal_length", y="sepal_width", data=data)
<AxesSubplot:xlabel='sepal_length', ylabel='sepal_width'>
>>> plt.title('Title using Matplotlib function')
Text(0.5, 1.0, 'Title using Matplotlib function')
>>> plt.show()
>>> 