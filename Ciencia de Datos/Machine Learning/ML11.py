Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> from sklearn.cluster import KMeans
>>> import matplotlib.image as img
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> image= img.imread("tiger.png")
>>> image.shape
(720, 1280, 3)
>>> plt.imshow(image)
<matplotlib.image.AxesImage object at 0x7fce66b488b0>
>>> plt.show()
>>> r=[]
>>> g=[]
>>> b=[]
>>> for row in image:
	for pixel in row:
		r.append(pixel[0])
		g.append(pixel[1])
		b.append(pixel[2])

	
>>> df= pd.DataFrame({'red':r,'green':g,'blue':b})
>>> df.head()
        red     green      blue
0  0.643137  0.627451  0.623529
1  0.647059  0.631373  0.627451
2  0.643137  0.639216  0.631373
3  0.647059  0.643137  0.635294
4  0.650980  0.647059  0.639216
>>> distortions = []
>>> num_clusters = range(1, 7)
>>> for i in num_clusters:
	cluster_centers, distortion = kmeans(df[['red','green','blue']].values.astype(float), i)
	distortions.append(distortion)

Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    cluster_centers, distortion = kmeans(df[['red','green','blue']].values.astype(float), i)
NameError: name 'kmeans' is not defined
>>> for i in num_clusters:
	cluster_centers, distortion = KMeans(df[['red','green','blue']].values.astype(float), i)
	distortions.append(distortion)

	
Traceback (most recent call last):
  File "<pyshell#33>", line 2, in <module>
    cluster_centers, distortion = KMeans(df[['red','green','blue']].values.astype(float), i)
TypeError: __init__() takes from 1 to 2 positional arguments but 3 were given
>>> cluster_centers, _ = KMeans(df[['red','green','blue']].values.astype(float), 2)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    cluster_centers, _ = KMeans(df[['red','green','blue']].values.astype(float), 2)
TypeError: __init__() takes from 1 to 2 positional arguments but 3 were given
>>> for i in num_clusters:
	cluster_centers, distortion = KMeans(df[['red','blue']].values.astype(float), i)
	distortions.append(distortion)

Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    cluster_centers, distortion = KMeans(df[['red','blue']].values.astype(float), i)
TypeError: __init__() takes from 1 to 2 positional arguments but 3 were given
>>> cluster_centers, _ = kmeans(df[['red','green','blue']].values.astype(float), 2)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    cluster_centers, _ = kmeans(df[['red','green','blue']].values.astype(float), 2)
NameError: name 'kmeans' is not defined
>>> cluster_centers, _ = KMeans(df[['red','green','blue']].values.astype(float), 2)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    cluster_centers, _ = KMeans(df[['red','green','blue']].values.astype(float), 2)
TypeError: __init__() takes from 1 to 2 positional arguments but 3 were given
>>> cluster_centers, _ = kmeans(df[['red','green','blue']].values.float()
	