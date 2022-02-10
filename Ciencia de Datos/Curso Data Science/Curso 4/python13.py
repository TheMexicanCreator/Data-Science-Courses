Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import random
>>> import numpy as np
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> from sklearn.cluster import KMeans
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    from sklearn.cluster import KMeans
ModuleNotFoundError: No module named 'sklearn'
>>> from sklearn.cluster import KMeans
>>> from sklearn.datasets.samples_generator import make_blobs
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    from sklearn.datasets.samples_generator import make_blobs
ModuleNotFoundError: No module named 'sklearn.datasets.samples_generator'
>>> from sklearn.datasets import make_blobs
>>> x1 = [-4.9, -3.5, 0, -4.5, -3, -1, -1.2, -4.5, -1.5, -4.5, -1, -2, -2.5, -2, -1.5, 4, 1.8, 2, 2.5, 3, 4, 2.25, 1, 0, 1, 2.5, 5, 2.8, 2, 2]
>>> x2 = [-3.5, -4, -3.5, -3, -2.9, -3, -2.6, -2.1, 0, -0.5, -0.8, -0.8, -1.5, -1.75, -1.75, 0, 0.8, 0.9, 1, 1, 1, 1.75, 2, 2.5, 2.5, 2.5, 2.5, 3, 6, 6.5]
>>> colors_map = np.array(['b', 'r'])
>>> def assign_members(x1, x2, centers):
	compare_to_first_center = np.sqrt(np.square(np.array(x1) - centers[0][0]) + np.square(np.array(x2) - centers[0][1]))
	compare_to_second_center = np.sqrt(np.square(np.array(x1) - centers[1][0]) + np.square(np.array(x2) - centers[1][1]))
	class_of_points = compare_to_first_center > compare_to_second_center
	colors = colors_map[class_of_points + 1 - 1]return colors, class_of_points
	
SyntaxError: invalid syntax
>>> def assign_members(x1, x2, centers):
	compare_to_first_center = np.sqrt(np.square(np.array(x1) - centers[0][0]) + np.square(np.array(x2) - centers[0][1]))
	compare_to_second_center = np.sqrt(np.square(np.array(x1) - centers[1][0]) + np.square(np.array(x2) - centers[1][1]))
	class_of_points = compare_to_first_center > compare_to_second_center
	colors = colors_map[class_of_points + 1 - 1]
	return colors, class_of_points

>>> print('assign_members function defined!')
assign_members function defined!
>>> def update_centers(x1, x2, class_of_points):
	center1 = [np.mean(np.array(x1)[~class_of_points]), np.mean(np.array(x2)[~class_of_points])]
	center2 = [np.mean(np.array(x1)[class_of_points]), np.mean(np.array(x2)[class_of_points])]
	return [center1, center2]

>>> def plot_points(centroids=None, colors='g', figure_title=None):
	fig = plt.figure(figsize=(15, 10))
	ax = fig.add_subplot(1, 1, 1)

	
>>> def plot_points(centroids=None, colors='g', figure_title=None):
	fig = plt.figure(figsize=(15, 10))
	ax = fig.add_subplot(1, 1, 1)
	centroid_colors = ['bx', 'rx']
	if centroids:
		for (i,centroid in enumerate(centroids)):
			
SyntaxError: invalid syntax
>>> def plot_points(centroids=None, colors='g', figure_title=None):
	fig = plt.figure(figsize=(15, 10))
	ax = fig.add_subplot(1, 1, 1)
	centroid_colors = ['bx', 'rx']
	if centroids:
		for (i, centroid) in enumerate(centroids):
			ax.plot(centroid[0], centroid[1], centroid_colors[i], markeredgewidth=5, markersize=20)
	plt.scatter(x1, x2, s=500, c=colors)
	xticks = np.linspace(-6, 8, 15, endpoint=True)
	yticks = np.linspace(-6, 6, 13, endpoint=True)
	ax.set_xticks(xticks)
	ax.set_yticks(yticks)
	xlabels = xticks
	ax.set_xticklabels(xlabels)
	ylabels = yticks
	ax.set_yticklabels(ylabels)
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	ax.tick_params('both', length=2, width=1, which='major', labelsize=15)
	ax.set_xlabel('x1', fontsize=20)
	ax.set_ylabel('x2', fontsize=20)
	ax.set_title(figure_title, fontsize=24)
	plt.show()

>>> plot_points(figure_title='Scatter Plot of x2 vs x1')
>>> centers = [[-2, 2], [2, -2]]
>>> plot_points(centers, figure_title='k-means Initialization')
>>> number_of_iterations = 4
>>> for i in range(number_of_iterations):
	input('Iteration {} - Press Enter to update the members of each cluster'.format(i + 1))
	colors, class_of_points = assign_members(x1, x2, centers)
	title = 'Iteration {} - Cluster Assignment'.format(i + 1)
	plot_points(centers, colors, figure_title=title)
	input('Iteration {} - Press Enter to update the centers'.format(i + 1))
	centers = update_centers(x1, x2, class_of_points)
	title = 'Iteration {} - Centroid Update'.format(i + 1)
	plot_points(centers, colors, figure_title=title)

Iteration 1 - Press Enter to update the members of each cluster
''
Iteration 1 - Press Enter to update the centers
''
Iteration 2 - Press Enter to update the members of each cluster

================================ RESTART: Shell ================================
>>> np.random.seed(0)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    np.random.seed(0)
NameError: name 'np' is not defined
>>> import numpy as np
>>> np.random.seed(0)
>>> X, y = make_blobs(n_samples=5000, centers=[[4, 4], [-2, -1], [2, -3], [1, 1]], cluster_std=0.9)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    X, y = make_blobs(n_samples=5000, centers=[[4, 4], [-2, -1], [2, -3], [1, 1]], cluster_std=0.9)
NameError: name 'make_blobs' is not defined
>>>  sklearn.datasets import make_blobs
 
SyntaxError: unexpected indent
>>> sklearn.datasets import make_blobs
SyntaxError: invalid syntax
>>> from sklearn.datasets import make_blobs
>>> X, y = make_blobs(n_samples=5000, centers=[[4, 4], [-2, -1], [2, -3], [1, 1]], cluster_std=0.9)
>>> plt.figure(figsize=(15, 10))
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    plt.figure(figsize=(15, 10))
NameError: name 'plt' is not defined
>>> import matplotlib.pyplot as plt
>>> plt.figure(figsize=(15, 10))
<Figure size 3000x2000 with 0 Axes>
>>> plt.scatter(X[:, 0], X[:, 1], marker='.')
<matplotlib.collections.PathCollection object at 0x7fbbb45fc490>
>>> plt.show()
>>> k_means = KMeans(init="k-means++", n_clusters=4, n_init=12)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    k_means = KMeans(init="k-means++", n_clusters=4, n_init=12)
NameError: name 'KMeans' is not defined
>>> from sklearn.cluster import KMeans
>>> k_means.fit(X)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    k_means.fit(X)
NameError: name 'k_means' is not defined
>>> k_means = KMeans(init="k-means++", n_clusters=4, n_init=12)
>>> k_means.fit(X)
KMeans(n_clusters=4, n_init=12)
>>> k_means_labels = k_means.labels_
>>> k_means_labels
array([0, 3, 3, ..., 1, 0, 0], dtype=int32)
>>> k_means_cluster_centers = k_means.cluster_centers_
>>> k_means_cluster_centers
array([[-2.03743147, -0.99782524],
       [ 3.97334234,  3.98758687],
       [ 0.96900523,  0.98370298],
       [ 1.99741008, -3.01666822]])
>>> fig = plt.figure(figsize=(15, 10))
>>> colors = plt.cm.Spectral(np.linspace(0, 1, len(set(k_means_labels))))
>>> ax = fig.add_subplot(1, 1, 1)
>>> for k, col in zip(range(len([[4,4], [-2, -1], [2, -3], [1, 1]])), colors):
	my_members = (k_means_labels == k)
	cluster_center = k_means_cluster_centers[k]
	ax.plot(X[my_members, 0], X[my_members, 1], 'w', markerfacecolor=col, marker='.')
	ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,  markeredgecolor='k', markersize=6)

[<matplotlib.lines.Line2D object at 0x7fbbb5517160>]
[<matplotlib.lines.Line2D object at 0x7fbbb55173d0>]
[<matplotlib.lines.Line2D object at 0x7fbbb55176d0>]
[<matplotlib.lines.Line2D object at 0x7fbbb55179a0>]
[<matplotlib.lines.Line2D object at 0x7fbbb5517c70>]
[<matplotlib.lines.Line2D object at 0x7fbbb5517f40>]
[<matplotlib.lines.Line2D object at 0x7fbbb5527250>]
[<matplotlib.lines.Line2D object at 0x7fbbb5527520>]
>>> ax.set_title('KMeans')
Text(0.5, 1.0, 'KMeans')
>>> ax.set_xticks(())
[]
>>> ax.set_yticks(())
[]
>>> plt.show()
>>> !wget -q -O 'customer_segmentation.csv' https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/labs/customer_segmentation.csv
SyntaxError: invalid syntax
>>> wget -q -O 'customer_segmentation.csv' https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/labs/customer_segmentation.csv
SyntaxError: invalid syntax
>>> 