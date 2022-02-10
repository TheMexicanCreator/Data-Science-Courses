Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import numpy as np
>>> import pandas as pd
>>> import folium
>>> world_map= folium.Map()
>>> print(world_map)
<folium.folium.Map object at 0x7fca7fa7b7f0>
>>> world_map
<folium.folium.Map object at 0x7fca7fa7b7f0>
>>> world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)
>>> world_map
<folium.folium.Map object at 0x7fca814d2e50>
>>> mexico_latitude= 23.6345
>>> mexico_longitude= -102.5528
>>> mexico_map= folium.Map(location= [mexico_laitude, mexico_longitude], zoom_start=4)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    mexico_map= folium.Map(location= [mexico_laitude, mexico_longitude], zoom_start=4)
NameError: name 'mexico_laitude' is not defined
>>> mexico_map= folium.Map(location= [mexico_latitude, mexico_longitude], zoom_start=4)
>>> mexico_map
<folium.folium.Map object at 0x7fca816e8b20>
>>> world_map= folium.Map(location= [56.130, -106.35], zoom_start= 4, titles='Stamen Toner')
>>> world_map
<folium.folium.Map object at 0x7fca816fff40>
>>> 
>>> #Ejercicio 2
>>> df_incidents= pd.read_csv('police.csv')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    df_incidents= pd.read_csv('police.csv')
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
FileNotFoundError: [Errno 2] No such file or directory: 'police.csv'
>>> de_incidents= pd.read_csv('police.csv')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    de_incidents= pd.read_csv('police.csv')
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
FileNotFoundError: [Errno 2] No such file or directory: 'police.csv'
>>> os.getcwd()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>> import os
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Curso Data Science/Extras')
>>> os.getcwd()
'/Users/robertogarcia/Documents/Curso Data Science/Extras'
>>> df_incidents= pd.read_csv('police.csv')
>>> df_incidents.head()
   Unnamed: 0  IncidntNum  ...                               Location          PdId
0           0   120058272  ...   (37.775420706711, -122.403404791479)  1.200580e+13
1           1   120058272  ...   (37.775420706711, -122.403404791479)  1.200580e+13
2           2   141059263  ...  (37.7299809672996, -122.388856204292)  1.410590e+13
3           3   160013662  ...  (37.7857883766888, -122.412970537591)  1.600140e+13
4           4   160002740  ...  (37.7650501214668, -122.419671780296)  1.600030e+13

[5 rows x 14 columns]
>>> df_incidents.shape()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    df_incidents.shape()
TypeError: 'tuple' object is not callable
>>> df_incidents.shape
(5, 14)
>>> limit=100
>>> df_incidents= df_incidents.iloc[0:limit, :]
>>> df_incidents.shape
(5, 14)
>>> latitude= 37.77
>>> longitude= -122.42
>>> sanfran_map= folium.map(location= [latitude,longitude], zoom_start=12)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    sanfran_map= folium.map(location= [latitude,longitude], zoom_start=12)
TypeError: 'module' object is not callable
>>> sanfran_map= folium.Map(location= [latitude,longitude], zoom_start=12)
>>> sanfran_map
<folium.folium.Map object at 0x7fca814d2df0>
>>> display(sanfran_map)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    display(sanfran_map)
NameError: name 'display' is not defined
>>> map.showMap()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    map.showMap()
AttributeError: type object 'map' has no attribute 'showMap'
>>> incidents = folium.map.FeatureGroup()
>>> for lat, lng, in zip(df_incidents.Y, df_incidents.X):
	incidents.add_child(
		folium.CircleMarker(
			[lat, lng],
			radius=5,
			color='yellow',
			fill=True,
			fill_color='blue',
			fill_opacity=0.6
		)
	)

<folium.map.FeatureGroup object at 0x7fca816d8fa0>
<folium.map.FeatureGroup object at 0x7fca816d8fa0>
<folium.map.FeatureGroup object at 0x7fca816d8fa0>
<folium.map.FeatureGroup object at 0x7fca816d8fa0>
<folium.map.FeatureGroup object at 0x7fca816d8fa0>
>>> sanfran_map.add_child(incidents)
<folium.folium.Map object at 0x7fca814d2df0>
>>> print(sanfran_map.add_child(incidents))
<folium.folium.Map object at 0x7fca814d2df0>
>>> 