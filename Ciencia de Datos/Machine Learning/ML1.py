Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import numpy as np
>>> import pandas as pd
>>> import os
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> df= pd.read_csv('SalaryGender.csv', delimiter= ',')
>>> salary= numpy.array(df['Salary'])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    salary= numpy.array(df['Salary'])
NameError: name 'numpy' is not defined
>>> salary= np.array(df['Salary'])
>>> gener= np.array(df['Gender'])
>>> phd= np.array(df['PhD'])
>>> age= np.array(df['Age'])
>>> print(df)
    Salary  Gender  Age  PhD
0    140.0       1   47    1
1     30.0       0   65    1
2     35.1       0   56    0
3     30.0       1   23    0
4     80.0       0   53    1
..     ...     ...  ...  ...
95    18.6       1   26    0
96   152.0       1   56    1
97     1.8       1   28    0
98    35.0       0   44    0
99     4.0       0   24    0

[100 rows x 4 columns]
>>> 
>>> #Ejercicio 2
>>> os.getcwd()
'/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning'
>>> df= pd.read_csv('mtcars.csv', delimiter= ',')
>>> data.head()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data.head()
NameError: name 'data' is not defined
>>> print(df)
                  model   mpg  cyl   disp   hp  ...   qsec  vs  am  gear  carb
0             Mazda RX4  21.0    6  160.0  110  ...  16.46   0   1     4     4
1         Mazda RX4 Wag  21.0    6  160.0  110  ...  17.02   0   1     4     4
2            Datsun 710  22.8    4  108.0   93  ...  18.61   1   1     4     1
3        Hornet 4 Drive  21.4    6  258.0  110  ...  19.44   1   0     3     1
4     Hornet Sportabout  18.7    8  360.0  175  ...  17.02   0   0     3     2
5               Valiant  18.1    6  225.0  105  ...  20.22   1   0     3     1
6            Duster 360  14.3    8  360.0  245  ...  15.84   0   0     3     4
7             Merc 240D  24.4    4  146.7   62  ...  20.00   1   0     4     2
8              Merc 230  22.8    4  140.8   95  ...  22.90   1   0     4     2
9              Merc 280  19.2    6  167.6  123  ...  18.30   1   0     4     4
10            Merc 280C  17.8    6  167.6  123  ...  18.90   1   0     4     4
11           Merc 450SE  16.4    8  275.8  180  ...  17.40   0   0     3     3
12           Merc 450SL  17.3    8  275.8  180  ...  17.60   0   0     3     3
13          Merc 450SLC  15.2    8  275.8  180  ...  18.00   0   0     3     3
14   Cadillac Fleetwood  10.4    8  472.0  205  ...  17.98   0   0     3     4
15  Lincoln Continental  10.4    8  460.0  215  ...  17.82   0   0     3     4
16    Chrysler Imperial  14.7    8  440.0  230  ...  17.42   0   0     3     4
17             Fiat 128  32.4    4   78.7   66  ...  19.47   1   1     4     1
18          Honda Civic  30.4    4   75.7   52  ...  18.52   1   1     4     2
19       Toyota Corolla  33.9    4   71.1   65  ...  19.90   1   1     4     1
20        Toyota Corona  21.5    4  120.1   97  ...  20.01   1   0     3     1
21     Dodge Challenger  15.5    8  318.0  150  ...  16.87   0   0     3     2
22          AMC Javelin  15.2    8  304.0  150  ...  17.30   0   0     3     2
23           Camaro Z28  13.3    8  350.0  245  ...  15.41   0   0     3     4
24     Pontiac Firebird  19.2    8  400.0  175  ...  17.05   0   0     3     2
25            Fiat X1-9  27.3    4   79.0   66  ...  18.90   1   1     4     1
26        Porsche 914-2  26.0    4  120.3   91  ...  16.70   0   1     5     2
27         Lotus Europa  30.4    4   95.1  113  ...  16.90   1   1     5     2
28       Ford Pantera L  15.8    8  351.0  264  ...  14.50   0   1     5     4
29         Ferrari Dino  19.7    6  145.0  175  ...  15.50   0   1     5     6
30        Maserati Bora  15.0    8  301.0  335  ...  14.60   0   1     5     8
31           Volvo 142E  21.4    4  121.0  109  ...  18.60   1   1     4     2

[32 rows x 12 columns]
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> plt.figure(figsize=(16,9))
<Figure size 3200x1800 with 0 Axes>
>>> sns.lineplot(x='model', y='hp', data=df1, marker='o', color='indigo')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    sns.lineplot(x='model', y='hp', data=df1, marker='o', color='indigo')
NameError: name 'df1' is not defined
>>> sns.lineplot(x='model', y='hp', data=df, marker='o', color='indigo')
<AxesSubplot:xlabel='model', ylabel='hp'>
>>> plt.tile('Horse Power')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    plt.tile('Horse Power')
AttributeError: module 'matplotlib.pyplot' has no attribute 'tile'
>>> plt.title('Horse Power')
Text(0.5, 1.0, 'Horse Power')
>>> plt.xticks(df1.model.unique(), rotation=45)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    plt.xticks(df1.model.unique(), rotation=45)
NameError: name 'df1' is not defined
>>> plt.xticks(df.model.unique(), rotation=45)
([<matplotlib.axis.XTick object at 0x7fc290e71820>, <matplotlib.axis.XTick object at 0x7fc290e717f0>, <matplotlib.axis.XTick object at 0x7fc290eaca60>, <matplotlib.axis.XTick object at 0x7fc291303ca0>, <matplotlib.axis.XTick object at 0x7fc291330400>, <matplotlib.axis.XTick object at 0x7fc291330b50>, <matplotlib.axis.XTick object at 0x7fc2913372e0>, <matplotlib.axis.XTick object at 0x7fc291337a30>, <matplotlib.axis.XTick object at 0x7fc29133d1c0>, <matplotlib.axis.XTick object at 0x7fc291337a90>, <matplotlib.axis.XTick object at 0x7fc2913308e0>, <matplotlib.axis.XTick object at 0x7fc29133d9a0>, <matplotlib.axis.XTick object at 0x7fc291343130>, <matplotlib.axis.XTick object at 0x7fc291343880>, <matplotlib.axis.XTick object at 0x7fc29134a0a0>, <matplotlib.axis.XTick object at 0x7fc29134a760>, <matplotlib.axis.XTick object at 0x7fc291343970>, <matplotlib.axis.XTick object at 0x7fc2913300a0>, <matplotlib.axis.XTick object at 0x7fc29134a2b0>, <matplotlib.axis.XTick object at 0x7fc291351310>, <matplotlib.axis.XTick object at 0x7fc291351a60>, <matplotlib.axis.XTick object at 0x7fc2913561f0>, <matplotlib.axis.XTick object at 0x7fc291356940>, <matplotlib.axis.XTick object at 0x7fc291351700>, <matplotlib.axis.XTick object at 0x7fc291343100>, <matplotlib.axis.XTick object at 0x7fc291356d30>, <matplotlib.axis.XTick object at 0x7fc2913604c0>, <matplotlib.axis.XTick object at 0x7fc291360c10>, <matplotlib.axis.XTick object at 0x7fc2913643a0>, <matplotlib.axis.XTick object at 0x7fc291360be0>, <matplotlib.axis.XTick object at 0x7fc291356e20>, <matplotlib.axis.XTick object at 0x7fc291364b80>], [Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, '')])
>>> plt.show()
>>> x=df['model'].values
>>> y= df['hp'].values
>>> fig, ax = plt.subplots(figsize =(12, 9))
>>> ax.barh(x, y, color='dodgerblue', edgecolor=(0,0,0))
<BarContainer object of 32 artists>
>>> ax.set_title('Horse Power')
Text(0.5, 1.0, 'Horse Power')
>>> plt.show()
>>> corr1= df.corr()
>>> corr1
           mpg       cyl      disp  ...        am      gear      carb
mpg   1.000000 -0.852162 -0.847551  ...  0.599832  0.480285 -0.550925
cyl  -0.852162  1.000000  0.902033  ... -0.522607 -0.492687  0.526988
disp -0.847551  0.902033  1.000000  ... -0.591227 -0.555569  0.394977
hp   -0.776168  0.832447  0.790949  ... -0.243204 -0.125704  0.749812
drat  0.681172 -0.699938 -0.710214  ...  0.712711  0.699610 -0.090790
wt   -0.867659  0.782496  0.887980  ... -0.692495 -0.583287  0.427606
qsec  0.418684 -0.591242 -0.433698  ... -0.229861 -0.212682 -0.656249
vs    0.664039 -0.810812 -0.710416  ...  0.168345  0.206023 -0.569607
am    0.599832 -0.522607 -0.591227  ...  1.000000  0.794059  0.057534
gear  0.480285 -0.492687 -0.555569  ...  0.794059  1.000000  0.274073
carb -0.550925  0.526988  0.394977  ...  0.057534  0.274073  1.000000

[11 rows x 11 columns]
>>> sns.heatmap(corr1, cmap="Reds")
<AxesSubplot:>
>>> my_labels= df['model']
>>> my_colors= ['mediumseagreen','mistyrose','teal','navajowhite','purple','gold','thistle','yellowgreen','orange','dimgray','sandybrown','red','cadetblue','pink','navy','mediumorchid','tan','blue','peru','darkgreen','darkorange','indianred' ,"darkseagreen",'saddlebrown','lightcoral','gray', 'slateblue','salmon']
>>> plot = df.plot.pie(y='hp', figsize=(15, 15),colors=my_colors, labels=my_labels, autopct='%1.1f%%', subplots=True)
>>> plt.show()
>>> df.hp.describe()
count     32.000000
mean     146.687500
std       68.562868
min       52.000000
25%       96.500000
50%      123.000000
75%      180.000000
max      335.000000
Name: hp, dtype: float64
>>> ordered=df.sort_values(by=['hp'], ascending=False)
>>> ordered=ordered.reset_index(drop=True)
>>> ordered
                  model   mpg  cyl   disp   hp  ...   qsec  vs  am  gear  carb
0         Maserati Bora  15.0    8  301.0  335  ...  14.60   0   1     5     8
1        Ford Pantera L  15.8    8  351.0  264  ...  14.50   0   1     5     4
2            Duster 360  14.3    8  360.0  245  ...  15.84   0   0     3     4
3            Camaro Z28  13.3    8  350.0  245  ...  15.41   0   0     3     4
4     Chrysler Imperial  14.7    8  440.0  230  ...  17.42   0   0     3     4
5   Lincoln Continental  10.4    8  460.0  215  ...  17.82   0   0     3     4
6    Cadillac Fleetwood  10.4    8  472.0  205  ...  17.98   0   0     3     4
7           Merc 450SLC  15.2    8  275.8  180  ...  18.00   0   0     3     3
8            Merc 450SE  16.4    8  275.8  180  ...  17.40   0   0     3     3
9            Merc 450SL  17.3    8  275.8  180  ...  17.60   0   0     3     3
10         Ferrari Dino  19.7    6  145.0  175  ...  15.50   0   1     5     6
11    Hornet Sportabout  18.7    8  360.0  175  ...  17.02   0   0     3     2
12     Pontiac Firebird  19.2    8  400.0  175  ...  17.05   0   0     3     2
13          AMC Javelin  15.2    8  304.0  150  ...  17.30   0   0     3     2
14     Dodge Challenger  15.5    8  318.0  150  ...  16.87   0   0     3     2
15            Merc 280C  17.8    6  167.6  123  ...  18.90   1   0     4     4
16             Merc 280  19.2    6  167.6  123  ...  18.30   1   0     4     4
17         Lotus Europa  30.4    4   95.1  113  ...  16.90   1   1     5     2
18            Mazda RX4  21.0    6  160.0  110  ...  16.46   0   1     4     4
19        Mazda RX4 Wag  21.0    6  160.0  110  ...  17.02   0   1     4     4
20       Hornet 4 Drive  21.4    6  258.0  110  ...  19.44   1   0     3     1
21           Volvo 142E  21.4    4  121.0  109  ...  18.60   1   1     4     2
22              Valiant  18.1    6  225.0  105  ...  20.22   1   0     3     1
23        Toyota Corona  21.5    4  120.1   97  ...  20.01   1   0     3     1
24             Merc 230  22.8    4  140.8   95  ...  22.90   1   0     4     2
25           Datsun 710  22.8    4  108.0   93  ...  18.61   1   1     4     1
26        Porsche 914-2  26.0    4  120.3   91  ...  16.70   0   1     5     2
27             Fiat 128  32.4    4   78.7   66  ...  19.47   1   1     4     1
28            Fiat X1-9  27.3    4   79.0   66  ...  18.90   1   1     4     1
29       Toyota Corolla  33.9    4   71.1   65  ...  19.90   1   1     4     1
30            Merc 240D  24.4    4  146.7   62  ...  20.00   1   0     4     2
31          Honda Civic  30.4    4   75.7   52  ...  18.52   1   1     4     2

[32 rows x 12 columns]
>>> AvgHP=ordered.loc[(ordered['hp'] >= 109) & (ordered['hp'] <= 180)]
>>> AvgHP=AvgHP.reset_index(drop=True)
>>> AvgHP
                model   mpg  cyl   disp   hp  ...   qsec  vs  am  gear  carb
0         Merc 450SLC  15.2    8  275.8  180  ...  18.00   0   0     3     3
1          Merc 450SE  16.4    8  275.8  180  ...  17.40   0   0     3     3
2          Merc 450SL  17.3    8  275.8  180  ...  17.60   0   0     3     3
3        Ferrari Dino  19.7    6  145.0  175  ...  15.50   0   1     5     6
4   Hornet Sportabout  18.7    8  360.0  175  ...  17.02   0   0     3     2
5    Pontiac Firebird  19.2    8  400.0  175  ...  17.05   0   0     3     2
6         AMC Javelin  15.2    8  304.0  150  ...  17.30   0   0     3     2
7    Dodge Challenger  15.5    8  318.0  150  ...  16.87   0   0     3     2
8           Merc 280C  17.8    6  167.6  123  ...  18.90   1   0     4     4
9            Merc 280  19.2    6  167.6  123  ...  18.30   1   0     4     4
10       Lotus Europa  30.4    4   95.1  113  ...  16.90   1   1     5     2
11          Mazda RX4  21.0    6  160.0  110  ...  16.46   0   1     4     4
12      Mazda RX4 Wag  21.0    6  160.0  110  ...  17.02   0   1     4     4
13     Hornet 4 Drive  21.4    6  258.0  110  ...  19.44   1   0     3     1
14         Volvo 142E  21.4    4  121.0  109  ...  18.60   1   1     4     2

[15 rows x 12 columns]
>>> AvgHP.describe()
             mpg        cyl        disp  ...         am       gear       carb
count  15.000000  15.000000   15.000000  ...  15.000000  15.000000  15.000000
mean   19.293333   6.666667  232.246667  ...   0.333333   3.600000   2.933333
std     3.789736   1.447494   92.933439  ...   0.487950   0.736788   1.279881
min    15.200000   4.000000   95.100000  ...   0.000000   3.000000   1.000000
25%    16.850000   6.000000  160.000000  ...   0.000000   3.000000   2.000000
50%    19.200000   6.000000  258.000000  ...   0.000000   3.000000   3.000000
75%    21.000000   8.000000  289.900000  ...   1.000000   4.000000   4.000000
max    30.400000   8.000000  400.000000  ...   1.000000   5.000000   6.000000

[8 rows x 11 columns]
>>> corr2=AvgHP.corr()
>>> sns.heatmap(corr2, cmap="Greens")
<AxesSubplot:>
>>> plt.show()
>>> my_labels2=AvgHP['model']
>>> my_colors2=['mistyrose','purple','gold','yellowgreen','orange','dimgray','red','cadetblue','pink','mediumorchid','tan','blue','darkgreen','darkorange','indianred' ,"darkseagreen",'saddlebrown','lightcoral','salmon']
>>> plot = AvgHP.plot.pie(y='hp', figsize=(10, 10), colors=my_colors2, labels=my_labels2, autopct='%1.1f%%', subplots=True)
>>> plt.show()
>>> 